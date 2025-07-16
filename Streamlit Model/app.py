import streamlit as st
import pandas as pd
import joblib

# --- PAGE CONFIG ---
st.set_page_config(page_title="Prediksi Nasabah Bank", layout="centered")

# --- CACHE ---
@st.cache_data
def load_data():
    return pd.read_csv("bank-additional-full_cleaned.csv")

@st.cache_resource
def load_model():
    return joblib.load("best_xgb_model.pkl", 'rb')

@st.cache_resource
def load_threshold():
    return joblib.load("best_threshold.pkl", 'rb')

data_ref = load_data()
model = load_model()
threshold = load_threshold()

# --- SESSION STATE ---
if "page" not in st.session_state:
    st.session_state.page = "home"

# --- SIDEBAR NAVIGATION ---
def change_page_to(page_name):
    st.session_state.page = page_name

if st.session_state.page != "home":
    with st.sidebar:
        st.header("Navigasi")

        if st.button("🏠 Kembali ke Halaman Utama"):
            st.session_state.page = "home"
            st.rerun()  # <- Tambahkan ini agar halaman langsung berpindah

        mode = st.radio("Pilih Mode Input", ["Manual", "CSV"], key="sidebar_mode")
        if mode == "Manual":
            change_page_to("manual")
        elif mode == "CSV":
            change_page_to("csv")


# --- HOME PAGE ---
if st.session_state.page == "home":
    st.title("📊 Prediksi Ketertarikan Nasabah terhadap Produk Bank")
    st.markdown("""
    Gunakan teknologi **Machine Learning** untuk memprediksi apakah nasabah akan tertarik pada produk bank.  
    Dengan memanfaatkan model prediktif ini, Anda bisa:
                
    - Menargetkan calon pelanggan yang potensial.
    - Menghemat biaya telemarketing.
    - Meningkatkan tingkat konversi penawaran produk.

    Akurasi model mencapai **±80%** berdasarkan hasil pelatihan dan evaluasi.
    Dalam Model ini ditambahkan juga Treshold, gunanya untuk menaikan precision dan menurnkan recall
    """)

    st.divider()
    st.markdown("### Klik tombol di bawah ini untuk mulai mengisi data nasabah.")
    if st.button("🔍 Mulai Prediksi"):
        st.session_state.page = "manual"

# --- MANUAL INPUT PAGE ---
elif st.session_state.page == "manual":
    st.title("🧍‍♂️ Prediksi - Input Manual")

    with st.form("form_manual"):
        col1, col2 = st.columns(2)
        with col1:
            age = st.number_input("Usia", 18, 100, 30)
            job = st.selectbox("Pekerjaan", sorted(data_ref["job"].unique()))
            marital = st.selectbox("Status Pernikahan", sorted(data_ref["marital"].unique()))
            education = st.selectbox("Pendidikan", sorted(data_ref["education"].unique()))
            default = st.selectbox("Memiliki Kredit Macet?", sorted(data_ref["default"].unique()))
            housing = st.selectbox("Memiliki Pinjaman Rumah?", sorted(data_ref["housing"].unique()))
            loan = st.selectbox("Memiliki Pinjaman Pribadi?", sorted(data_ref["loan"].unique()))
            contact = st.selectbox("Jenis Kontak", sorted(data_ref["contact"].unique()))

        with col2:
            month = st.selectbox("Bulan Kontak Terakhir", sorted(data_ref["month"].unique()))
            day_of_week = st.selectbox("Hari Kontak Terakhir", sorted(data_ref["day_of_week"].unique()))
            duration = st.number_input("Durasi Kontak (detik)", 0, 5000, 100)
            campaign = st.number_input("Jumlah Kontak dalam Kampanye Ini", 1, 50, 1)
            previous = st.number_input("Jumlah Kontak Sebelumnya", 0, 100, 0)
            poutcome = st.selectbox("Hasil Kontak Sebelumnya", sorted(data_ref["poutcome"].unique()))
            emp_var_rate = st.number_input("Variasi Tingkat Kerja", -3.0, 3.0, 1.1)
            cons_price_idx = st.number_input("Indeks Harga Konsumen", 90.0, 100.0, 93.2)
            cons_conf_idx = st.number_input("Indeks Kepercayaan Konsumen", -50.0, 0.0, -36.4)
            euribor3m = st.number_input("Tingkat Euribor 3 Bulan", 0.0, 6.0, 4.8)
            nr_employed = st.number_input("Jumlah Pegawai", 4000.0, 5500.0, 5191.0)

        submit_manual = st.form_submit_button("🔍 Prediksi")

    if submit_manual:
        try:
            input_df = pd.DataFrame([{
                "age": age, "job": job, "marital": marital, "education": education,
                "default": default, "housing": housing, "loan": loan, "contact": contact,
                "month": month, "day_of_week": day_of_week, "duration": duration,
                "campaign": campaign, "previous": previous, "poutcome": poutcome,
                "emp_var_rate": emp_var_rate, "cons_price_idx": cons_price_idx,
                "cons_conf_idx": cons_conf_idx, "euribor3m": euribor3m, "nr_employed": nr_employed
            }])
            proba = model.predict_proba(input_df)[0][1]
            pred = 1 if proba >= threshold else 0
            label = "✅ Nasabah *Tertarik*" if pred == 1 else "❌ Nasabah *Tidak Tertarik*"
            st.success(f"{label} ({proba * 100:.2f}%) - Threshold: {threshold}")
        except Exception as e:
            st.error(f"Gagal memproses prediksi: {e}")

# --- CSV INPUT PAGE ---
elif st.session_state.page == "csv":
    st.title("📁 Prediksi - Upload File CSV")
    st.markdown("Unggah file CSV dengan kolom yang sesuai format data pelatihan.")

    min_age, max_age = st.slider("Filter Rentang Usia", 18, 100, (18, 100))

    uploaded_file = st.file_uploader("Pilih file CSV", type=["csv"])
    if uploaded_file:
        try:
            df_input = pd.read_csv(uploaded_file)

            if not all(col in df_input.columns for col in data_ref.columns):
                st.warning("Kolom dalam file CSV tidak lengkap atau tidak sesuai format.")
            else:
                # Filter berdasarkan usia
                df_input = df_input[(df_input["age"] >= min_age) & (df_input["age"] <= max_age)]

                if df_input.empty:
                    st.warning("Tidak ada data dalam rentang usia tersebut.")
                else:
                    st.success("File berhasil dimuat. Memproses prediksi...")

                    probs = model.predict_proba(df_input)[:, 1]
                    preds = (probs >= threshold).astype(int)

                    df_input["Probabilitas_Tertarik"] = probs
                    df_input["Prediksi"] = ["Tertarik" if p == 1 else "Tidak Tertarik" for p in preds]

                    total = len(df_input)
                    total_ya = sum(preds)
                    total_tidak = total - total_ya
                    persen = total_ya / total * 100

                    untung = 477
                    rugi = -23
                    estimasi = total_ya * untung + total_tidak * rugi

                    st.info(f"""
                        Dari jumlah **{total} orang** (usia {min_age}–{max_age}):
                        - Prediksi: **{total_ya} orang** menerima tawaran (**{persen:.2f}%**)
                        - Prediksi: **{total_tidak} orang** menolak tawaran
                        - 💰 Estimasi keuntungan: **${estimasi:,.2f}**
                    """)

                    st.dataframe(df_input)

                    # Hanya hasil prediksi YA yang bisa diunduh
                    df_download = df_input[df_input["Prediksi"] == "Tertarik"]
                    csv_out = df_download.to_csv(index=False).encode("utf-8")
                    st.download_button(
                        "💾 Unduh Hasil Prediksi (Hanya Tertarik)",
                        data=csv_out,
                        file_name="hasil_prediksi_ya_saja.csv",
                        mime="text/csv"
                    )

        except Exception as e:
            st.error(f"Gagal memproses file: {e}")
