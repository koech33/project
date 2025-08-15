import streamlit as st
# import pandas as pd
# import time
# @st.dialog("Data Collection")
# def data_collection() :
#     county = st.text_input('Enter county name')
#     town = st.text_input('Enter town name')
#     if st.button('Submit Details'):
#         if county and town :
#             st.write(f"Were glad you're from {county} in {town}")
#         else:
#             st.write('You need to enter county name, town name')
#
#
#
#
#
#
st.title("Sleep")
st.write("Welcome to The Sleep Prediction App.")

# st.header("")
# st.subheader("Sub Header")
# st.write("Emmanuel Koech!")
# st.caption("Koech!")
#
# st.code("""
# import streamlit as st
# st.title("Title")
# st.header("Header")
# st.subheader("Sub Header")
# st.write("Emmanuel Koech!")
# st.caption("Koech!")
# st.title("Title")
# """)
#
# with st.echo():
#     st.write("The code is both executed and displayed")
#
# st.divider()
# st.subheader("Sub Header")
# st.write("--------------")
#
# df = pd.read_csv("data.csv")
# st.dataframe(df)
# edited_df = st.data_editor(df)
# st.write("Edited Dataframe")
# st.dataframe(edited_df)
# #st.table(edited_df)
# st.metric("Temperature", 16 , -2)
# st.metric("Humidity in %", 77 , 8)
# if     st.button("Submit"):
#     st.write("Form has been submitted")
# st.write("What are your thoughts on the photo")
# user_feedback = st.feedback()
# st.write(user_feedback)
# if user_feedback == 1:
#     st.write("Thank you for liking me!")
# elif user_feedback == 0:
#     st.write("Thank you for your feedback, well try to improve our content")
# st.write("Give your rating")
# stars = st.feedback("stars")
# st.write(stars)
#
# if stars == 0:
#     st.write("Youve given 1 star")
# elif stars == 1:
#     st.write("Youve given 2 star")
# elif stars == 2:
#     st.write("Youve given 3 stars")
# elif stars == 3:
#     st.write("Youve given 4 stars")
# elif stars == 4:
#     st.write("Youve given 5 stars")
# else:
#     pass
#
# terms_and_conditions=st.checkbox("I agree to the terms and conditions")
# if terms_and_conditions:
#     st.write("You agree to the terms and conditions")
# st.toggle("Dark Mode")
#
# gender = st.radio("Select your gender", ["Male", "Female"])
# if gender == "Male":
#     st.write("You've been drafted.")
# elif gender == "Female":
#     st.write("You're required to offer medical assistance.")
#
# team = st.selectbox("Select your team", ["United", "City","Liverpool","Arsenal"])
# if team == "United":
#     st.write("Glory Glory Man United")
# elif team == "City":
#     st.write("Glory Glory Man City")
# elif team == "Liverpool":
#     st.write("Glory Glory Man Liverpool")
#
#
# breakfast = st.multiselect("What did breakfast",["Sausage","Eggs","Bacon","Bread"])
#
# st.write(breakfast)
# st.select_slider("Shirt size",["XL","L","M","S","XS"])
# age = st.number_input("Enter your age", 1,100,20)
# KCPE = st.slider("Enter your KCPE marks",0,500,300)
# date = st.date_input("Enter the date today")
# time2 = st.time_input("Enter your time")
# name = st.text_input("Enter your name")
# if name :
#     st.write(f"Hello, {name}  welcome to my streamlit app")
#
# st.text_area("Enter your article here :",height=300)
#
# uploaded_file = st.file_uploader("Upload your file")
#
# #st.camera_input("Take a photo")
# st.image("Project Overview.png")
#
# col1, col2, col3 = st.columns(3)
# with col1:
#     first_name =st.text_input("Enter your first name")
# with col2:
#     second_name=st.text_input("Enter your second name")
# with col3:
#     #st.button("PPost")
#     email_address=st.text_input("Enter your email address")
#
#
# dialog_box = st.selectbox("Do you want the dialog box?",["Yes","No"])
# if dialog_box == "No":
#     pass
# else:
#     data_collection()
#
# with st.expander("Click to see more details"):
#     st.write("Some content")
#     st.write("Some content")
#     st.write("Some content")
#     st.write("Some content")
#     st.write("Some content")
#
# with st.popover("settings"):
#     st.checkbox("Show completed")
#
# #with st.sidebar:
#     #st.write("This is the sidebar")
#
# #with st.spinner("Running"):
#    # time.sleep(3)
#    # st.write("This is the spinner")
#
#
#
# #progress_text = "Operation in Progress"
# #progress_bar = st.progress(0, text = progress_text)
#
# st.toast("Welcome Home", icon = "✨")
# st.write("He was crowned champion! :crown:")
# st.balloons()
# st.success("You've successfully signed up!")
# st.error("You're cureently using the free version")
# st.info("You're healthy")
# st.warning("You're not cureently using the free version")
