import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load the model
Model = pickle.load(open("knn_model.pkl", "rb"))

# App title
st.title("🏦 Bankruptcy Prevention System")

# User inputs
st.header("Enter Company Financial Data")
industrial_risk = st.number_input("industrial_risk")
management_risk = st.number_input(" management_risk")
financial_flexibility = st.number_input(" financial_flexibility")
credibility = st.number_input(" credibility")
competitiveness = st.number_input(" competitiveness")
operating_risk = st.number_input(" operating_risk")
Class = st.number_input("Class")

# Prediction
if st.button("Predict"):
    input_data = np.array([['industrial_risk', ' management_risk', ' financial_flexibility',
       ' credibility', ' competitiveness', ' operating_risk', 'Class']])  # reshape for model
    prediction = Model.predict(input_data)[0]
    if prediction == 1:
        st.error("⚠ The company is at risk of bankruptcy.")
    else:
        st.success("✅ The company is financially safe.")
