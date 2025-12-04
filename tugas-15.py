import streamlit as st

st.title("Form Data Diri")
st.write("Silakan isi data diri Anda:")
st.write("Made by Keysha")

with st.form("Form Data Diri"):
    name = st.text_input("Nama")
    alamat = st.text_input("Alamat")
    usia = st.number_input("Usia")
    submit = st.form_submit_button("Submit")

if submit :
    st.success("Data berhasil disubmit!")