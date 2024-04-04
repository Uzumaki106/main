import streamlit as st
st.title("WELCOME TO PREDICTION MODEL")
sl=st.selectbox('SELECT ANY ONE MODEL',['Disease Prediction','Flower Prediction','Image Recognition'])
bl=st.button("SUBMIT")
if bl==True :
    st.write('Welcome To ',sl,' Model')
    st.balloons()