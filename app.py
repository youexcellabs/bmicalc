import streamlit as st

st.title('BMI Calculator')

weight = st.number_input("Enter your weight in (KG)")
height = st.number_input("Enter your height in (m)")

if height > 0:
    bmi = weight/ (height**2)
    st.write(f"Your BMI is {bmi}")
    if bmi < 70:
        st.write("Your BMI is Normal")
    elif bmi > 70:
        st.write("Your BMI is in Critical stage")