import streamlit as st
import pandas as pd
import pickle

# Load the churn prediction model
model = pickle.load(open("churn_model.pkl", "rb"))

# Define the app title and header
st.title("Customer Churn Prediction App")
st.header("Predict whether a customer is likely to churn or stay")

# Create input fields for customer data
credit_score = st.number_input("Credit score", min_value=0, step=1)
country_options = {"France": 1, "Spain": 2, "Germany": 3}
country = st.selectbox("Country", list(country_options.keys()))
gender_options = {"Male": 0, "Female": 1}
gender = st.selectbox("Gender", list(gender_options.keys()))
age = st.number_input("Age", min_value=18, step=1)
tenure = st.number_input("Tenure", min_value=0, step=1)
balance = st.number_input("Balance", format="%.2f")
products_number = st.number_input("Number of products", min_value=0, step=1)
credit_card = st.selectbox("Has credit card", ["Yes", "No"])
active_member = st.selectbox("Active member", ["Yes", "No"])
estimated_salary = st.number_input("Estimated salary", format="%.2f")

# Collect input data into a dictionary, converting selected options to numbers
customer_data = {
    "CreditScore": credit_score,
    "Geography_Spain": 1 if country == "Spain" else 0,
    "Geography_Germany": 1 if country == "Germany" else 0,
    "Gender_Male": 1 if gender == "Male" else 0,
    "Age": age,
    "Tenure": tenure,
    "Balance": balance,
    "NumOfProducts": products_number,
    "HasCrCard": 1 if credit_card == "Yes" else 0,
    "IsActiveMember": 1 if active_member == "Yes" else 0,
    "EstimatedSalary": estimated_salary,
}

# Create a button to trigger prediction
if st.button("Predict Churn"):
    prediction = model.predict(pd.DataFrame([customer_data]))[0]
    if prediction == 1:
        st.write("**Customer will churn.**")
    else:
        st.write("**Customer will stay.**")