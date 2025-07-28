# 🔐 Suspicious Web Threat Detector

A machine learning-powered web traffic analyzer that detects and classifies suspicious activity using both unsupervised (Isolation Forest) and supervised (Random Forest) techniques. Built with Python, Streamlit, SHAP, and Scikit-learn.

---

## 🚀 Features

- 📊 **Anomaly Detection** using Isolation Forest
- 🧠 **Classification** with Random Forest
- 🔍 **Explainability** via SHAP (feature importance)
- 💡 **Interactive Web App** using Streamlit
- 📈 Visualizations of traffic patterns and anomalies

---

## 📁 Dataset

The app uses a sample network traffic dataset from AWS WAF logs (`CloudWatch_Traffic_Web_Attack.csv`) which includes fields like:

- IP addresses
- Session durations
- Packet sizes
- Detection type (`waf_rule` for flagged threats)

---

## 🛠️ Tech Stack

- Python (Pandas, NumPy)
- Scikit-learn (ML models)
- SHAP (model explainability)
- Streamlit (dashboard)
- Matplotlib, Seaborn (visuals)

---

## 💻 How to Run Locally

### ▶️ 1. Clone the repository

```bash
git clone https://github.com/ychaitanya0823/suspicious-threat-detector.git
cd suspicious-threat-detector
