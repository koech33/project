import streamlit as st
import pickle
import pandas as pd
import numpy as np
from dotenv import load_dotenv
st.header("Quality of Sleep Predictor")
with open("svm.pkl", "rb") as f:
    loaded_model = pickle.load(f)
import streamlit as st
import pickle
import numpy as np

# Load the trained pipeline (preprocessing + model)
with open("svm.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Quality of Sleep Prediction App 🛌💤")

st.write("Fill in your details to predict the quality of sleep.")

# Replace with the exact features you trained on
feature_names = [
    "Gender",                # categorical
    "Age",                   # numeric
    "Occupation",            # categorical
    "Sleep Duration",        # numeric
    "Physical Activity Level",# numeric
    "Stress Level",          # numeric
    "BMI Category",          # categorical
    "Heart Rate",            # numeric
    "Daily Steps"            # numeric
]

# Collect inputs — use text for categories, number_input for numeric
inputs = []
for feature in feature_names:
    if feature in ["Gender", "Occupation", "BMI Category"]:
        value = st.text_input(f"Enter {feature}:")
    else:
        value = st.number_input(f"Enter {feature}:", value=0.0)
    inputs.append(value)

# Reshape into (1, -1) for prediction
input_array = np.array(inputs).reshape(1, -1)

# Predict
if st.button("Predict"):
    prediction = model.predict(input_array)
    st.success(f"Predicted Quality of Sleep: {prediction[0]}")
