import streamlit as st
st.title('a small program')
st.subheader('I am Suu Wai Moe')
st.write('My first streamlit app')
st.write('You have to enter your scores for each subject.')
Myanmar= st.number_input('Enter Myanmar Score:')
English= st.number_input('Enter English score:')
Maths = st.number_input('Enter Maths Score:')
Chemistry = st.number_input('Enter Chemistry Score:')
Physics = st.number_input('Enter Physics Score:')
Bio = st.number_input('Enter Bio Score:')
if Myanmar >= 40 and English >= 40 and Maths >= 40 and Chemistry >= 40 and Physics >= 40 and Bio >= 40:
    st.write("You've passed the exam")
    if Myanmar >= 75:
        st.write('Myanmar Distinction')
    if English >= 75:
        st.write('English Distinction')
    if Maths >= 80:
        st.write('Maths Distinction')
    if Chemistry >= 80:
        st.write('Chemistry Distinction')
    if Physics >= 80:
        st.write('Physics Distinction')
    if Bio >= 75:
        st.write('Bio Distinction')
else:
    st.write("You fail the exam")
Total_Score=Myanmar+English+Maths+Chemistry+Physics+Bio
st.write('Your total score:',Total_Score)