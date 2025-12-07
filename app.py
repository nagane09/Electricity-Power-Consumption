from flask import Flask, request, render_template
import pandas as pd
import joblib
import os

app = Flask(__name__)

MODEL_PATH = "power_model.joblib"

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError("Model file missing!")

model = joblib.load(MODEL_PATH)

@app.route("/", methods=["GET", "POST"])
def home():
    prediction_text = ""
    if request.method == "POST":
        try:
            # Collect input from form
            input_data = pd.DataFrame([{
                "Temperature": float(request.form["Temperature"]),
                "Humidity": float(request.form["Humidity"]),
                "WindSpeed": float(request.form["WindSpeed"]),
                "GeneralDiffuseFlows": float(request.form["GeneralDiffuseFlows"]),
                "DiffuseFlows": float(request.form["DiffuseFlows"]),
                "Day": int(request.form["Day"]),
                "Month": int(request.form["Month"]),
                "Year": int(request.form["Year"]),
                "Hour": int(request.form["Hour"]),
                "Minute": int(request.form["Minute"])
            }])

            # Predict
            prediction = model.predict(input_data)[0]
            prediction_text = f"Predicted Power Consumption: {prediction:.2f} kW"

        except Exception as e:
            prediction_text = f"Error: {e}"

    return render_template("index.html", prediction_text=prediction_text)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
