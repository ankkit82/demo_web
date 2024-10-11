import streamlit as st

name = st.text_input("Enter your name :")
fname = st.text_input("Enter your Father name :")
adr = st.text_area("Enter your address :")
classdata = st.selectbox("Enter your class :",(1,2,3,4,5,6,7,8,9,10,11,12))

button = st.button("submit")
if button:
    st.markdown("""
    Name : {name}
    father name : {fname}
    address : {adr}
    class : {classdata}""")