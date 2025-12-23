# Travel-Package-Purchase-Prediction


🔗 **Live Demo:**  
https://electricity-power-consumption.onrender.com/

-----

# ⚡ Power Consumption Prediction System

A complete **end-to-end Machine Learning project** that predicts **power consumption (Zone 1)** using environmental and temporal features.  
The project includes **data preprocessing, model comparison, model selection, and deployment using Flask**.

---

## 📌 Project Overview

Accurate power consumption forecasting is critical for:
- Energy management
- Load balancing
- Cost optimization

This project builds and deploys a **regression-based ML system** that predicts power consumption based on:
- Weather conditions
- Diffuse solar flows
- Date and time features

---

## 🧠 Machine Learning Pipeline

### 1️⃣ Data Collection
- Dataset: `powerconsumption.csv`
- Records: **52,416**
- Target variable: `PowerConsumption_Zone1`

### 2️⃣ Feature Engineering
The original `Datetime` column is decomposed into:
- `Day`
- `Month`
- `Year`
- `Hour`
- `Minute`

Final input features:
- Temperature
- Humidity
- WindSpeed
- GeneralDiffuseFlows
- DiffuseFlows
- Day, Month, Year
- Hour, Minute

---

### 3️⃣ Data Preprocessing
- Removed unused zones (Zone 2 & Zone 3)
- No missing values
- Standardized numerical features using **StandardScaler**
- Train-test split: **75% train / 25% test**

---

## 📊 Model Training & Evaluation

Multiple regression models were trained and evaluated using:
- Mean Squared Error (MSE)
- Mean Absolute Error (MAE)
- R² Score

### 🔍 Model Performance Summary

| Model | Train R² | Test R² |
|------|--------|--------|
| Linear Regression | 0.639 | 0.642 |
| Ridge Regression | 0.639 | 0.642 |
| Lasso Regression | 0.639 | 0.642 |
| Decision Tree | **1.000** | 0.966 |
| Random Forest | **0.998** | **0.983** |
| KNN | 0.939 | 0.903 |
| XGBoost | 0.983 | 0.977 |

---

### ✅ Final Model Selection
The **Random Forest Regressor** was selected due to:
- Highest generalization performance
- Low prediction error
- Robustness to non-linear relationships

The trained model was saved as:
```bash
power_model.joblib
```

----

# Power Consumption Prediction

🔮 **Model Inference Pipeline**  

During prediction:

- User inputs data via a web form
- Inputs are converted into a Pandas DataFrame
- Model performs regression inference
- Output is returned as predicted power consumption (kW)

🌐 **Flask Web Application**  

The model is deployed using Flask for real-time prediction.

🧩 **App Features**  

- HTML form for user input
- Backend validation & error handling
- Displays predicted power consumption instantly

🧪 **Flask Route Logic**  

**GET:** Renders input form  

**POST:**  
- Collects user inputs  
- Converts them to numerical format  
- Predicts power consumption using the trained model  



🧠 **Mathematical Intuition (High-Level)**  

The final model (Random Forest) works by:

- Training multiple decision trees on random subsets of data
- Averaging predictions to reduce variance  

🚀 **Future Improvements**  

- Hyperparameter tuning with GridSearchCV  
- Time-series specific models (LSTM, Prophet)  
- Feature importance visualization  
- Docker-based deployment  
- REST API integration  

🛠️ **Tech Stack**  

- Python  
- Pandas, NumPy  
- Scikit-learn  
- XGBoost  
- Flask  
- Joblib  
- HTML/CSS
