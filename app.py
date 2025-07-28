# app.py
import streamlit as st
import pandas as pd
import shap
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

st.set_page_config(page_title="Web Threat Detector", layout="centered")

st.title("🔐 Suspicious Web Threat Detector")
st.write("Upload web traffic CSV file to detect suspicious activities.")

# Upload CSV
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    # Load Data
    df = pd.read_csv(uploaded_file)

    # Data Preprocessing
    df['creation_time'] = pd.to_datetime(df['creation_time'])
    df['end_time'] = pd.to_datetime(df['end_time'])
    df['session_duration'] = (df['end_time'] - df['creation_time']).dt.total_seconds()
    df['session_duration'].replace(0, 0.001, inplace=True)
    df['avg_packet_size'] = (df['bytes_in'] + df['bytes_out']) / df['session_duration']
    df['is_suspicious'] = (df['detection_types'] == 'waf_rule').astype(int)

    # Features and Labels
    features = ['bytes_in', 'bytes_out', 'session_duration', 'avg_packet_size']
    X = df[features]
    y = df['is_suspicious']

    # Split and Train Model
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    predictions = model.predict(X)

    # Output
    df['Prediction'] = predictions
    st.success("✅ Prediction Completed!")
    st.dataframe(df[['bytes_in', 'bytes_out', 'session_duration', 'avg_packet_size', 'Prediction']])

    # SHAP Explainability
    st.subheader("🔍 Feature Importance (SHAP)")
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X)
    shap.summary_plot(shap_values, X, plot_type="bar", show=False)
    st.pyplot(plt)
