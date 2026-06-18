
import streamlit as st

st.title("Tính thuế thu nhập cá nhân")

luong = st.number_input("Nhập thu nhập", min_value=0.0)

if st.button("Tính thuế"):
    thue = luong * 0.1
    st.write("Thuế phải nộp:", thue)
