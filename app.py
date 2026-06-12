import streamlit as st
import joblib
import pandas as pd


model = joblib.load('model_churn.pkl')


st.set_page_config(page_title="Churn Analytics", page_icon="📊")
st.title("📊 Aplikasi Prediksi Churn Pelanggan")
st.markdown("""
Aplikasi ini menggunakan **Machine Learning** untuk memprediksi 
apakah seorang pelanggan memiliki risiko tinggi untuk berhenti berlangganan.
""")
st.write("---")


st.subheader("Masukkan Data Pelanggan Terbaru:")

tenure = st.slider("Lama Berlangganan (Bulan)", min_value=0, max_value=72, value=12)
monthly_charges = st.number_input("Tagihan Bulanan ($)", min_value=0.0, max_value=150.0, value=65.0)
total_charges = st.number_input("Total Tagihan ($)", min_value=0.0, max_value=8000.0, value=tenure * monthly_charges)

st.write("---")


if st.button("Analisis Risiko Pelanggan", type="primary"):
    
    
    data_input = pd.DataFrame([{
        'tenure': tenure,
        'MonthlyCharges': monthly_charges,
        'TotalCharges': total_charges
    }])
    
    
    peluang_churn = model.predict_proba(data_input)[0][1]
    persentase = peluang_churn * 100
    
    st.subheader("Hasil Analisis AI:")
    
    
    if peluang_churn > 0.5:
        st.error(f"🚨 **Risiko Tinggi!** Pelanggan ini memiliki peluang **{persentase:.1f}%** untuk berhenti.")
        st.markdown("* **Rekomendasi:** Berikan promo khusus atau diskon perpanjangan kontrak.")
    else:
        st.success(f"✅ **Risiko Rendah.** Pelanggan ini relatif aman dengan peluang pindah hanya **{persentase:.1f}%**.")