import streamlit as st
import pickle
import numpy as np

# Load the model
Model = pickle.load(open("knn_model.pkl", "rb"))

# App title
st.title("🏦 Bankruptcy Prevention System")

# User inputs
st.header("Enter Company Financial Data")
industrial_risk = st.number_input("Industrial Risk", value=0.0)
management_risk = st.number_input("Management Risk", value=0.0)
financial_flexibility = st.number_input("Financial Flexibility", value=0.0)
credibility = st.number_input("Credibility", value=0.0)
competitiveness = st.number_input("Competitiveness", value=0.0)
operating_risk = st.number_input("Operating Risk", value=0.0)

# Prediction
if st.button("Predict"):
    # Create numeric array
    input_data = np.array([[industrial_risk, management_risk, financial_flexibility,
                            credibility, competitiveness, operating_risk]])
    
    prediction = Model.predict(input_data)[0]

    if prediction == 1:
        st.error("⚠ The company is at risk of bankruptcy.")
    else:
        st.success("✅ The company is financially safe.")
