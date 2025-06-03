import streamlit as st
import pandas as pd

#file = st.file_uploader("Upload CSV File")
file = st.sidebar("Upload CSV File")

if file:
    data = pd.read_csv(file)
    #st.write("Full Data:")
    st.dataframe(data)
