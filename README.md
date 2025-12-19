# Travel-Package-Purchase-Prediction


🔗 **Live Demo:**  
https://electricity-power-consumption.onrender.com/

---

# Electricity Power Consumption Prediction

A machine learning project that **analyzes and predicts electricity power consumption** patterns using real electricity usage datasets. This project explores historical data, performs feature extraction, builds predictive models, and outputs forecasts and insights that help with energy planning and efficiency.

---

## 🚀 Project Summary

Electricity consumption forecasting is essential for:
* Energy providers planning supply
* Households and businesses managing usage
* Governments and utilities making policy decisions

This project builds predictive models to understand and forecast electricity usage based on historical data and time‑series characteristics.

## 📊 What This Project Does

1. **Exploratory Data Analysis**
   - Visualize consumption patterns over time
   - Identify trends, seasonality, and anomalies

2. **Data Preprocessing**
   - Clean missing values
   - Convert timestamps into features (hour, day, month)
   - Scale numerical variables

3. **Feature Engineering**
   - Create lag features (past usage)
   - Extract useful time‑based signals

4. **Model Training & Selection**
   - Train regression models to predict consumption
   - Compare performance of different algorithms
   - Select the best performing model

5. **Prediction & Output**
   - Generate future estimates of power consumption
   - Save predictions for reporting or visualization

---

## 📈 Model Results & Performance

### 🔹 Random Forest Regressor

**Training Data**
- Mean Squared Error (MSE): 727,393.27  
- Mean Absolute Error (MAE): 621.59  
- R² Score: 0.9857  

**Test Data**
- Mean Squared Error (MSE): 1,394,858.79  
- Mean Absolute Error (MAE): 842.64  
- R² Score: 0.9727  

> ✅ High R² and relatively low error indicate strong predictive performance with good generalization.

---

### 🔹 XGBoost Regressor (XGBClassifier)

**Training Data**
- Mean Squared Error (MSE): 361.56  
- Mean Absolute Error (MAE): 12.70  
- R² Score: 1.0000  

**Test Data**
- Mean Squared Error (MSE): 671,538.37  
- Mean Absolute Error (MAE): 544.46  
- R² Score: 0.9869  

> ✅ XGBoost shows excellent fit and high accuracy on test data, making it highly suitable for electricity consumption forecasting.

---

## 🛠 Technologies Used

- **Python** – Core programming language  
- **Pandas & NumPy** – Data manipulation and numerical computations  
- **scikit-learn** – Random Forest, model evaluation  
- **XGBoost** – Gradient boosting model  
- **Matplotlib & Seaborn** – Data visualization  
- **Jupyter Notebook** – Interactive experimentation  
- **CSV Files** – Dataset storage and prediction outputs  

---

## 📊 Example Use Cases

This electricity consumption forecasting system can be applied in:

- **Utility Grid Management:** Forecast energy demand and optimize supply  
- **Smart Homes & IoT:** Optimize appliance usage and reduce costs  
- **Renewable Energy Planning:** Match solar/wind generation with predicted demand  
- **Energy Policy & Research:** Study consumption trends and improve efficiency  




