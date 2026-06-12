# 📊 Telecom Customer Churn Prediction App

Sistem Kecerdasan Buatan (AI) berbasis web yang dirancang untuk memprediksi probabilitas pelanggan berhenti berlangganan (*churn*) pada perusahaan telekomunikasi.

## 🎯 1. Masalah Bisnis (Business Problem)
Mengakuisisi pelanggan baru membutuhkan biaya hingga **5 kali lipat lebih mahal** dibandingkan mempertahankan pelanggan yang sudah ada. Jika perusahaan tidak bisa memprediksi siapa saja pelanggan yang kecewa atau ingin pindah vendor, perusahaan akan kehilangan pendapatan secara drastis.

**Solusi:** Aplikasi ini bertindak sebagai *Early Warning System* untuk mendeteksi pelanggan berisiko tinggi secara *real-time*, sehingga tim marketing bisa langsung memberikan intervensi berupa promo/diskon tepat sasaran.

## 🛠️ 2. Teknologi & Library yang Digunakan
* **Python** (Bahasa Pemrograman Utama)
* **Google Colab & Scikit-Learn** (Analisis Data & Pelatihan Model AI)
* **Random Forest Classifier** (Algoritma Machine Learning)
* **Streamlit** (Pembuatan Antarmuka Aplikasi Web)

## 📁 3. Struktur File Proyek
* `app.py` - Kode utama untuk antarmuka aplikasi web menggunakan Streamlit.
* `model_churn.pkl` - File biner hasil ekspor "otak" Machine Learning dari Google Colab.
* `requirements.txt` - Daftar library Python yang dibutuhkan untuk menjalankan aplikasi.

## 📈 4. Cara Menjalankan Proyek Secara Lokal
1. Clone atau download repository ini.
2. Install dependensi: `pip install -r requirements.txt`
3. Jalankan aplikasi: `streamlit run app.py`# telecom-customer-churn-prediction
Aplikasi Machine Learning berbasis Web untuk memprediksi risiko pelanggan berhenti berlangganan
