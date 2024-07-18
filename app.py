import streamlit as st
import pickle

f=open("salary-model.pkl","rb")
mymodel=pickle.load(f)
mymetadata=pickle.load(f)
f.close()


def predict_salary(years):
    return mymodel.predict([[years]])[0]

st.title("Salary prediction")

years = st.number_input('Enter the experience in years')

if st.button('Predict Salary'):
    salary = predict_salary(years)
    st.write(f"The salary for {years} experience is {salary}")