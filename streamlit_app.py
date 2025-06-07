import streamlit as st

st.title("--Selamat Datang Di Web Informatika--")
st.write("ngoding seru bersama Satrio .")
st.image("IMG_3224.jpeg",width=500)

st.title("Aplikasi Sederhana")
st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis Sebuah Angka:", value=0, step=1)

if (angka % 2) == 0:
  st.write(f"{angka} adalah Bilangan Genap")
else:
  st.write(f"{angka} adalah bilangan
