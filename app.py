import streamlit as st

st.title("Main Area")

user_name = st.sidebar.text_input("Enter your name")
value = st.sidebar.slider("Choose a value", 0, 100)

st.write(f"Hello, {user_name}!")
st.write(f"Selected value: {value}")
