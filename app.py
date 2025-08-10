import streamlit as st
import pickle
import numpy as np

# Load model
Model = pickle.load(open("knn_model.pkl", "rb"))

# Mapping dictionary (must match training encoding)
risk_mapping = {"low": 0, "medium": 0.5, "high": 1}

st.title("🏦 Bankruptcy Prevention System")
st.header("Enter Company Financial Data")

industrial_risk = st.selectbox("Industrial Risk", ["low", "medium", "high"])
management_risk = st.selectbox("Management Risk", ["low", "medium", "high"])
financial_flexibility = st.selectbox("Financial Flexibility", ["low", "medium", "high"])
credibility = st.selectbox("Credibility", ["low", "medium", "high"])
competitiveness = st.selectbox("Competitiveness", ["low", "medium", "high"])
operating_risk = st.selectbox("Operating Risk", ["low", "medium", "high"])

if st.button("Predict"):
    # Convert inputs to numeric
    input_data = np.array([[risk_mapping[industrial_risk],
                            risk_mapping[management_risk],
                            risk_mapping[financial_flexibility],
                            risk_mapping[credibility],
                            risk_mapping[competitiveness],
                            risk_mapping[operating_risk]]])
    
    prediction = Model.predict(input_data)[0]

    if prediction == 1:
        st.error("⚠ The company is at risk of bankruptcy.")
    else:
        st.success("✅ The company is financially safe.")
