import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib

df = pd.read_csv("processed_data.csv")
rfm = pd.read_csv("rfm_model.csv")
pkl = joblib.load("clv_model.pkl")

st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Go to", ["Overview", "Customer Segmentation", "CLV Prediction"])


if page == "Overview":
    st.title("Overview")
    st.dataframe(df)    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Customers", df['CustID'].nunique())
    col2.metric("Total Revenue", f"£{df['Revenue'].sum():,.2f}")
    col3.metric("Total Transactions", df['Invoice'].nunique())
    
    st.subheader("Monthly Revenue Trend")
    monthly = df.groupby(['Year', 'Month'])['Revenue'].sum().reset_index()
    monthly['Date'] = pd.to_datetime(monthly[['Year', 'Month']].assign(day=1))
    monthly = monthly.sort_values('Date')

    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(monthly['Date'], monthly['Revenue'])
    ax.set_title('Monthly Revenue Trend')
    ax.set_xlabel('Date')
    ax.set_ylabel('Revenue')
    plt.tight_layout()
    st.pyplot(fig)


elif page == "Customer Segmentation":
    st.title("Customer Segmentation")
    
    st.subheader("Segment Distribution")
    seg_counts = rfm['Segment'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(seg_counts, labels=seg_counts.index, autopct='%1.1f%%')
    ax.set_title('Customer Segments')
    st.pyplot(fig)
    
    st.subheader("RFM Table")
    st.dataframe(rfm[['CustID', 'Recency', 'Frequency', 'Monetary', 'Segment']])
    
elif page == "CLV Prediction":
    st.title("CLV Prediction")
    
    st.subheader("Enter Customer Details")
    recency = st.slider("Recency (days since last purchase)", 1, 500, 30)
    frequency = st.slider("Frequency (number of orders)", 1, 200, 10)
    monetary = st.slider("Monetary (total spend £)", 1, 50000, 1000)
    
    if st.button("Predict CLV"):
        input_data = pd.DataFrame([[recency, frequency, monetary, 0, 0]], columns=['Recency', 'Frequency', 'Monetary', 'Cluster', 'Segment_encoded'])
        prediction = pkl.predict(input_data)[0]
        st.success(f"Predicted Future Revenue: £{prediction:,.2f}")