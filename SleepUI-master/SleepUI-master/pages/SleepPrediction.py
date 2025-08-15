import streamlit as st
import pickle
import numpy as np

with open("md.pkl", "rb") as f:
    model = pickle.load(f)

with open("saler.pkl", "rb") as f:
    scaler = pickle.load(f)

st.set_page_config(page_title="Sleep Quality Prediction", page_icon="✨")
st.title("💤 Sleep Quality Prediction")

# Input fields
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", min_value=0, max_value=120, value=25)
occupation = st.selectbox("Occupation", ["Doctor", "Engineer", "Lawyer", "Nurse", "Teacher","Software Engineer","Accountant","Scientist","Salesperson","Manager","Sales Representative"
])  
sleep_duration = st.number_input("Sleep Duration (hours)", min_value=0, max_value=24, value=7)
physical_activity = st.slider("Physical Activity Level (20=Low, 100=High)", 20, 100, 60)
stress_level = st.slider("Stress Level (1=Low, 10=High)", 1, 10, 5)
bmi_category = st.selectbox("BMI Category", ["Normal Weight", "Overweight", "Obese"])
heart_rate = st.number_input("Heart Rate", min_value=60, max_value=90, value=70)
daily_steps = st.slider("Daily Steps", min_value=1000, max_value=10000, value=5000)
bp_status = st.selectbox("Blood Pressure Status", ["Normal", "High", "Elevated"])
sleep_disorder= st.selectbox("Sleep Disorder", ["No Sleep Disorder", "Sleep Apnea", "Insomnia"])
# Map categorical variables to numbers

gender_map = {"Male":1,"Female":0}
occupation_map ={"Doctor":1,"Engineer":2,"Lawyer":3,"Nurse":5,"Teacher":10,"Software Engineer":9,"Accountant":0,"Scientist":8,"Salesperson":7,"Manager":4,"Sales Representative":6  }
bmi_map = {"Normal Weight":0, "Overweight":1, "Obese":2}
bp_map = {"Normal":2, "Elevated":0, "High":1}
sleep_disorder_map = {"No Sleep Disorder": 2, "Sleep Apnea": 1,"Insomnia":0}
input_data = np.array([[
    gender_map[gender],
    age,
    occupation_map[occupation],
    sleep_duration,
    physical_activity,
    stress_level,
    bmi_map[bmi_category],
    heart_rate,
    daily_steps,
    bp_map[bp_status],
    sleep_disorder_map[sleep_disorder]
]])
input_scaled = scaler.transform(input_data)
if st.button("Predict"):
    prediction = model.predict(input_scaled)
    st.success(f"Predicted Quality of Sleep: {prediction[0]}")