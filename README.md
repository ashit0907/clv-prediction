# Customer Lifetime Value (CLV) Prediction & Segmentation

## Overview
An end-to-end machine learning project that predicts the future revenue of customers and segments them into meaningful groups using RFM analysis and K-Means clustering.

## Live Demo
[Click here to view the app](https://clv-prediction-7a9ryeg3gnkyylsvmwegab.streamlit.app/)

## Problem Statement
Businesses need to identify their most valuable customers and predict future spending to optimize marketing strategies. This project solves that using real UK e-commerce transaction data.

## Dataset
- **Source:** Online Retail II UCI Dataset (Kaggle)
- **Size:** 1M+ transactions (2009-2011)
- **Features:** Invoice, StockCode, Description, Quantity, InvoiceDate, Price, Customer ID, Country

## Project Flow
1. Data Cleaning & Preprocessing
2. Exploratory Data Analysis (9 visualizations)
3. RFM Feature Engineering
4. Customer Segmentation using K-Means Clustering
5. CLV Prediction using Regression Models
6. Streamlit Dashboard with Deployment

## Customer Segments
| Segment | Description |
|---|---|
| VIP | Highest spenders, most frequent buyers |
| Champions | High value, recent buyers |
| At Risk | Used to buy regularly, now inactive |
| Lost | Haven't purchased in a long time |

## Models Used
| Model | R2 Score | RMSE |
|---|---|---|
| Linear Regression | 0.855 | 2863 |
| Random Forest | 0.929 | 1995 |
| XGBoost | 0.761 | 3666 |

**Best Model: Random Forest (Cross Validated R2: 0.59)**

## Tech Stack
- Python, Pandas, NumPy
- Scikit-learn, XGBoost
- Matplotlib, Seaborn
- Streamlit

## How to Run Locally
```bash
git clone https://github.com/yourusername/clv-prediction
cd clv-prediction
pip install -r requirements.txt
streamlit run app.py
```

## Key Insights
- Revenue peaks every October-November (holiday season)
- 98.9% customers are At Risk or Lost — retention is critical
- Monetary value is the strongest predictor of future CLV
- Top 4 VIP customers generate disproportionate revenue

## Author
Ashit Nayak — [LinkedIn](https://www.linkedin.com/in/ashit-nayak-955b90313/?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3B%2BUrnLwzKTXiSAk9YXV3dfg%3D%3D) | [GitHub](https://github.com/ashit0907)
