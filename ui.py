import streamlit as st
import requests
import json

st.header("Payment Fraud Detection App")

payment_type_mapping = {
    "CASH_OUT": 1,
    "PAYMENT": 2,
    "CASH_IN": 3,
    "TRANSFER": 4,
    "DEBIT": 5,
}

type = st.selectbox(label = "Payment Method", options = ["CASH_OUT", "PAYMENT", "CASH_IN", "TRANSFER", "DEBIT"])
type_numeric = payment_type_mapping.get(type, 0) 

amount = st.number_input(
    label = "Amount Paid",
    min_value = 0.00, 
    max_value = 92445516.64, 
    value = 1860.00
    )

oldbalanceOrg = st.number_input(
    label = "Sender's Initial Account Balance",
    min_value = 0.00, 
    value = 21240.00
    )

newbalanceOrig = st.number_input(
    label = "Sender's Final Account Balance",
    min_value = 0.00, 
    value = 19380.00
    )

oldbalanceDest = st.number_input(
    label = "Recipient's Initial Account Balance",
    min_value = 0.00, 
    value = 0.00
    )

newbalanceDest = st.number_input(
    label = "Recipient's Final Account Balance",
    min_value = 0.00, 
    value = 1860.00
    )

detector = st.button(label="Detect Fraud")

if detector:
    input_df = {
        "type": type_numeric,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest}

    url = st.secrets["API_URL"]

    response = requests.post(url, json=input_df)
    isFraud = response.json()["isFraud"]
    
    st.markdown(f'<p style="font-size:30px; color:black;">{isFraud}</p>', unsafe_allow_html=True)