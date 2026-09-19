from fastapi import FastAPI
import pandas as pd
import joblib


from app.schemas import Customer

# Creating the web application
app = FastAPI(
    title="Customer Purchase Prediction API",
    description="ML API for predicting customer purchases",
    version="1.0"
)

# Loading the model at the start itself
model = joblib.load(
    "model/customer_purchase_model.pkl"
)

# This is simple an health/ check endpoint
@app.get("/")
def home():
    return {
        "message": "Customer Purchase Prediction API is running."
    }

# This is our prediction endpoint
@app.post("/predict")
def predict(customer: Customer):

    data = pd.DataFrame([customer.model_dump()])

    # Prediction
    prediction = model.predict(data)[0]

    # Probability for the new data
    probability = model.predict_proba(data)[0][1]

    return {
        "prediction": int(prediction),
        "purchase_probability": float(probability)
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }