import streamlit as st
st.title ("Welcome to my quiz, are you ready ? Let's begin! ")

st.subheader("Question 1 : ")
with st.form("question1"):
    reponse1 = st.text_input("What is the name of Harry’s pet owl? ")
    button = st.form_submit_button("Confirm")
if button:
    if reponse1.lower() == "hedwig":
        st.write("Right answer ! ")
    else:
        st.write("Wrong answer ! ")

st.subheader("Question 2 : ")
with st.form("question2"):
    reponse2 = st.text_input("Who is Harry’s godfather? ")
    button = st.form_submit_button("Confirm")
if button:
    if reponse2.lower() == "sirius black":
        st.write("Right answer ! ")
    else:
        st.write("Wrong answer ! ")

st.subheader("Question 3 : ")
with st.form("question3"):
    reponse3 = st.text_input("What position does Harry play in Quidditch? ")
    button = st.form_submit_button("Confirm")
if button:
    if reponse3.lower() == "seeker":
        st.write("Right answer ! ")
    else:
        st.write("Wrong answer ! ")