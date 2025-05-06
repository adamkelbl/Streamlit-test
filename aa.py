import streamlit as st
import pandas as pd

# Načti data
@st.cache_data
def load_data():
    return pd.read_csv("/Users/adamkelbl/Desktop/textil.csv")

df = load_data()

st.title("📦 Report zásob metrového textilu")

# Zobrazit celý přehled
st.subheader("Celý seznam produktů")
st.dataframe(df)

# Filtr: Minimum odběr > zásoba
st.subheader("⚠️ MinimumAmount > Stock")
mask = (df['minimumamount'] > df['stock']) & (df['stock'] > 0)
st.dataframe(df[mask])