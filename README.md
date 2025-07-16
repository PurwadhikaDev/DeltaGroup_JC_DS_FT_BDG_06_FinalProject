# Optimalisasi Strategi Telemarketing Produk Deposito Berjangka melalui Model Prediktif Berbasis Data
Proyek ini merupakan bagian dari Proyek Akhir dalam program Digital Talent Incubator yang diselenggarakan oleh Purwadhika Digital Technology School.
Sebagai bagian dari proses analisis data, studi ini menggunakan dataset kampanye pemasaran perbankan. Untuk mendapatkan gambaran lebih lengkap mengenai struktur dan isi data yang digunakan, dapat merujuk pada dokumen Presentasi Kampanye Pemasaran Bank yang telah disusun secara terpisah.

# **Gambaran Umum**
Proyek ini berfokus pada pengembangan model machine learning untuk memprediksi apakah seorang nasabah akan berlangganan produk deposito berjangka setelah dihubungi melalui kampanye telemarketing.
Tujuan utama dari proyek ini adalah untuk meningkatkan efektivitas strategi telemarketing yang dijalankan oleh Bank portugal, dengan cara meningkatkan tingkat konversi pelanggan serta mengoptimalkan Return on Marketing Investment (ROMI) agar dapat mencapai atau melampaui standar rata-rata industri perbankan.

# **Business Problem**
## **Portugal Banking Campaign Opportunity**

Industri perbankan di Eropa, khususnya Portugal, mengalami transformasi signifikan pasca krisis keuangan dan pandemi. Salah satu pendekatan pemasaran yang masih relevan dan berdampak besar adalah kampanye pemasaran langsung melalui telepon (telemarketing) untuk produk simpanan berjangka (term deposit). Meskipun metode ini dianggap konvensional, pendekatan tersebut masih menunjukkan efektivitas tinggi dalam mencapai nasabah potensial, terutama untuk produk finansial yang membutuhkan penjelasan rinci.

Menurut laporan dari European Banking Federation (2023), strategi personalisasi dan pemanfaatan data historis pelanggan merupakan faktor kunci dalam meningkatkan keberhasilan kampanye pemasaran di sektor keuangan. Data dari kampanye pemasaran bank di Portugal yang dikumpulkan oleh UCI Machine Learning Repository menunjukkan bahwa meskipun sebagian besar pelanggan dihubungi melalui telepon, hanya sekitar 11,3% yang akhirnya menyetujui untuk membuka rekening deposito berjangka.

Fakta ini mengindikasikan adanya kebutuhan untuk memahami lebih dalam faktor-faktor apa saja yang mempengaruhi keputusan pelanggan. Dengan pemanfaatan teknik analisis data dan model prediktif, institusi keuangan dapat meningkatkan efektivitas kampanye, mengurangi biaya pemasaran, dan meningkatkan conversion rate.

## **Term Deposit Campaign Problem**

Salah satu tantangan utama dalam kampanye pemasaran produk deposito berjangka di sektor perbankan adalah rendahnya tingkat konversi nasabah. Banyak nasabah yang menolak penawaran, meskipun mereka termasuk dalam target pasar yang relevan. Hal ini kemungkinan besar disebabkan oleh pendekatan pemasaran yang belum cukup personal, waktu yang tidak tepat dalam menghubungi, atau kurangnya informasi tentang preferensi dan kebutuhan pelanggan.

Studi oleh Gensler et al. (2012) menunjukkan bahwa keberhasilan kampanye pemasaran sangat tergantung pada kemampuan untuk menyegmentasi pelanggan dan menyampaikan pesan pada waktu yang tepat. Ketidakefisienan dalam menyasar pelanggan yang memiliki potensi tinggi menyebabkan tingginya biaya operasional dan rendahnya return on investment (ROI) dari kampanye.

## **Problem Statement**

Bank menghadapi tantangan dalam menentukan calon pelanggan mana yang memiliki kemungkinan tinggi untuk menerima penawaran deposito berjangka. Ketidaktepatan dalam target kampanye mengakibatkan pemborosan sumber daya dan menurunkan efektivitas kampanye pemasaran.

## **Goals**

Berdasarkan permasalahan tersebut, tujuan utama dari analisis ini adalah mengembangkan model klasifikasi yang dapat memprediksi kemungkinan seorang pelanggan akan menerima penawaran deposito berjangka. Model ini akan didasarkan pada data demografi, status pekerjaan, riwayat interaksi pemasaran sebelumnya, dan variabel lainnya yang tersedia dalam dataset.

Dengan model ini, tim pemasaran dapat lebih fokus menyasar pelanggan yang memiliki potensi lebih tinggi untuk melakukan konversi, sehingga meningkatkan efisiensi kampanye dan meningkatkan tingkat keberhasilan pemasaran produk perbankan.

## **Matrix Evaluation**

### Conversion Rate Calculation

Conversion rate merupakan indikator kinerja utama (Key Performance Indicator/KPI) dalam kampanye pemasaran yang menunjukkan persentase pelanggan yang mengambil tindakan yang diharapkan dalam hal ini, `berlangganan deposito berjangka` dibandingkan dengan total pelanggan yang dihubungi.

$$
\text{Conversion Rate} = \left( \frac{\text{Jumlah pelanggan yang berlangganan}}{\text{Total pelanggan yang dihubungi}} \right) \times 100\%
$$

Data kampanye aktual dari Portugal (UCI Machine Learning Repository) menunjukkan bahwa dari seluruh pelanggan yang dihubungi, hanya sekitar 11,27% yang setuju untuk membuka rekening deposito berjangka.   
Meskipun angka ini dapat dikatakan mencerminkan hasil yang moderat, konversi ini masih tertinggal jika dibandingkan dengan performa industri keuangan yang lebih tinggi. Menurut laporan Ruler Analytics (2023), tingkat konversi rata-rata pada kampanye keuangan berkinerja tinggi dapat mencapai 23%.

Gap ini mengindikasikan adanya peluang besar untuk meningkatkan efektivitas strategi telemarketing melalui pendekatan berbasis data yang lebih presisi.

### ROMI Calculation

Return on Marketing Investment (ROMI) adalah metrik penting untuk mengukur berapa banyak keuntungan yang dihasilkan dari investasi pemasaran. ROMI menjadi alat strategis untuk menilai efektivitas kampanye, merencanakan alokasi anggaran masa depan, dan membandingkan kinerja antar saluran pemasaran.

$$
\text{ROMI} = \left( \frac{\text{Pendapatan yang dihasilkan} - \text{Biaya pemasaran}}{\text{Biaya pemasaran}} \right) \times 100\%
$$

Hasil perhitungan menunjukkan bahwa ROMI Electric Bank saat ini berada di angka 144,92%. Artinya, untuk setiap 1 euro yang dikeluarkan dalam kampanye telemarketing, bank menghasilkan 1,45 euro keuntungan bersih.
Namun, angka ini masih berada di bawah standar industri, di mana ROMI yang dianggap "baik" untuk industri keuangan adalah 5:1 (500%) atau lebih, menurut laporan oleh Improvado (2023).

Data ini menunjukkan adanya ruang signifikan untuk meningkatkan profitabilitas dari aktivitas pemasaran, terutama dengan mengoptimalkan sasaran pelanggan dan meminimalkan pemborosan biaya operasional melalui pendekatan analitik yang lebih cerdas.


### Cost Analysis

Sebelum membangun model machine learning, dilakukan analisis bisnis awal untuk memahami dampak finansial dari setiap keputusan prediksi dalam kampanye telemarketing.

- Asumsi Biaya dan Pendapatan.
    Berdasarkan studi oleh Moro, Cortez, & Rita (2014):

    - Biaya satu kali panggilan telemarketing: 23 euro
    - Pendapatan dari satu pelanggan yang berhasil berlangganan: 500 euro


- Simulasi Biaya dan Keuntungan Berdasarkan Jenis Prediksi.

    | Jenis Prediksi          | Penjelasan                                                            | Net Gain  |
    | ------------------------| --------------------------------------------------------------------- | --------- |
    | **True Positive (TP)**  | Pelanggan diprediksi akan berlangganan, dan benar-benar melakukannya. | +477 euro |
    | **False Positive (FP)** | Pelanggan diprediksi akan berlangganan, tapi ternyata tidak.          | −23 euro  |
    | **True Negative (TN)**  | Pelanggan diprediksi tidak akan berlangganan, dan memang tidak.       | 0 euro    |
    | **False Negative (FN)** | Pelanggan diprediksi tidak akan berlangganan, tapi seharusnya ya.     | 0 euro    |


- Metrik Evaluasi yang dipilih.

    - Precision :
        - Karena setiap False Positive menyebabkan kerugian langsung berupa biaya telemarketing yang tidak menghasilkan pendapatan, maka Precision (presisi) adalah metrik evaluasi yang paling tepat
        - Dengan precision tinggi, kita memastikan bahwa prediksi pelanggan yang berpotensi melakukan langganan benar-benar tepat, sehingga biaya pemasaran tidak terbuang sia-sia dan ROI meningkat.

## **Stakeholder**

Stakeholder utama dalam proyek pengembangan model prediktif ini adalah manajemen pemasaran dari institusi perbankan. Tim manajemen pemasaran bertanggung jawab dalam merancang, mengimplementasikan, dan mengevaluasi strategi kampanye pemasaran produk keuangan termasuk penawaran deposito berjangka melalui telemarketing.

Melalui model ini, kami bertujuan untuk memberikan dukungan berbasis data guna membantu manajemen pemasaran dalam:

- Mengidentifikasi calon pelanggan yang paling berpotensi untuk dikonversi

- Mengoptimalkan alokasi sumber daya pemasaran

- Meningkatkan efisiensi dan efektivitas kampanye

- Meminimalkan biaya yang timbul akibat panggilan yang tidak membuahkan hasil

Dengan pendekatan analitik yang tepat, diharapkan tim manajemen dapat mengambil keputusan yang lebih akurat dan strategis dalam menjalankan program pemasaran berikutnya.

## **Sumber Referensi**

- Ruler Analytics (2023). What Is a Good Conversion Rate for Financial Services? https://www.ruleranalytics.com

- Chaffey, D. (2019). Digital Marketing: Strategy, Implementation and Practice. Pearson Education.

- Improvado (2023). What Is a Good ROMI? Understanding Marketing ROI Benchmarks. https://improvado.io

- Kotler, P., & Keller, K. L. (2016). Marketing Management (15th ed.). Pearson Education.

- Kumar, V., & Petersen, A. (2012). Statistical Methods in Customer Relationship Management. Wiley.

- Moro, S., Laureano, R. M. S., & Cortez, P. (2014). Using data mining for bank direct marketing: An application of the CRISP-DM methodology. Expert Systems with Applications, 41(7),     3128-3141. https://doi.org/10.1016/j.eswa.2013.10.005

- Moro, S., Cortez, P., & Rita, P. (2014). A data-driven approach to predict the success of bank telemarketing. Decision Support Systems, 62, 22–31.https://doi.org/10.1016/j.dss.2014.01.006

- Gensler, S., Verhoef, P. C., & Böhm, M. (2012). Understanding consumers' multichannel choices across the different stages of the buying process. Marketing Letters, 23, 987–1003. https://doi.org/10.1007/s11002-012-9199-9

- European Banking Federation. (2023). Banking in Europe: EBF Facts & Figures. Brussels: EBF Publications. Retrieved from https://www.ebf.eu

- Baesens, B. (2014). Analytics in a Big Data World: The Essential Guide to Data Science and its Applications. Hoboken: Wiley.

- UCI Machine Learning Repository. (2024). Bank Marketing Dataset. Retrieved from https://archive.ics.uci.edu/ml/datasets/bank+marketing
