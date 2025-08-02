streamlit run app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cấu hình hiển thị
st.set_page_config(page_title="Telco Customer Churn Visualization", layout="wide")
sns.set(style="whitegrid")

# Tiêu đề ứng dụng
st.title("📊 Telco Customer Churn Dashboard")
st.markdown("This dashboard visualizes customer churn behavior from the Telco dataset.")

# Tải dữ liệu
@st.cache_data
def load_data():
    return pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

df = load_data()

# Tạo cột chia giao diện
col1, col2 = st.columns(2)

# Biểu đồ 1: Customer Churn Count
with col1:
    st.subheader("1. Customer Churn Count")
    fig1, ax1 = plt.subplots()
    sns.countplot(data=df, x='Churn', palette='Set2', ax=ax1)
    ax1.set_xlabel("Churn")
    ax1.set_ylabel("Count")
    ax1.set_title("Customer Churn Count")
    st.pyplot(fig1)

# Biểu đồ 2: Churn by Contract Type
with col2:
    st.subheader("2. Churn by Contract Type")
    fig2, ax2 = plt.subplots()
    sns.countplot(data=df, x='Contract', hue='Churn', palette='Set1', ax=ax2)
    ax2.set_title("Churn by Contract Type")
    ax2.set_xlabel("Contract Type")
    ax2.set_ylabel("Count")
    plt.setp(ax2.get_xticklabels(), rotation=15)
    st.pyplot(fig2)

# Biểu đồ 3: Distribution of Monthly Charges
st.subheader("3. Distribution of Monthly Charges")
fig3, ax3 = plt.subplots()
sns.histplot(df['MonthlyCharges'], kde=True, color='skyblue', ax=ax3)
ax3.set_title("Distribution of Monthly Charges")
ax3.set_xlabel("Monthly Charges")
ax3.set_ylabel("Frequency")
st.pyplot(fig3)

# Biểu đồ 4: Tenure by Churn Status
st.subheader("4. Tenure by Churn Status")
fig4, ax4 = plt.subplots()
sns.boxplot(data=df, x='Churn', y='tenure', palette='Set3', ax=ax4)
ax4.set_title("Tenure by Churn Status")
ax4.set_xlabel("Churn")
ax4.set_ylabel("Tenure (months)")
st.pyplot(fig4)

# Biểu đồ 5: Churn by Internet Service Type
st.subheader("5. Churn by Internet Service Type")
fig5, ax5 = plt.subplots()
sns.countplot(data=df, x='InternetService', hue='Churn', palette='pastel', ax=ax5)
ax5.set_title("Churn by Internet Service Type")
ax5.set_xlabel("Internet Service")
ax5.set_ylabel("Count")
st.pyplot(fig5)
