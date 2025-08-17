import streamlit as st
import pandas as pd
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Streamlit title
st.title("🎓 Student Performance Analysis")

st.write("Fill in the details below to predict the student's performance.")

# Input fields (same as Flask form)
gender = st.selectbox("Gender", ["male", "female"])
ethnicity = st.selectbox(
    "Race/Ethnicity",
    ["group A", "group B", "group C", "group D", "group E"]
)
parental_level_of_education = st.selectbox(
    "Parental Level of Education",
    [
        "some high school",
        "high school",
        "some college",
        "associate's degree",
        "bachelor's degree",
        "master's degree"
    ]
)
lunch = st.selectbox("Lunch", ["standard", "free/reduced"])
test_preparation_course = st.selectbox(
    "Test Preparation Course", ["none", "completed"]
)

# Numeric inputs
reading_score = st.number_input("Reading Score", min_value=0, max_value=100, value=50)
writing_score = st.number_input("Writing Score", min_value=0, max_value=100, value=50)

# Prediction button
if st.button("Predict"):
    try:
        # Build CustomData object (same as in Flask)
        data = CustomData(
            gender=gender,
            race_ethnicity=ethnicity,
            parental_level_of_education=parental_level_of_education,
            lunch=lunch,
            test_preparation_course=test_preparation_course,
            reading_score=reading_score,
            writing_score=writing_score
        )

        # Convert to dataframe
        pred_df = data.get_data_as_data_frame()

        # Run prediction
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)

        # Show result
        st.success(f"✅ Predicted Score: {results[0]}")
    except Exception as e:
        st.error(f"❌ Error during prediction: {e}")








# from flask import Flask,request,render_template
# import numpy as np
# import pandas as pd

# from sklearn.preprocessing import StandardScaler
# from src.pipeline.predict_pipeline import CustomData,PredictPipeline

# application=Flask(__name__)

# app=application

# ## Route for a home page

# @app.route('/')
# def index():
#     return render_template('index.html') 

# @app.route('/predictdata',methods=['GET','POST'])
# def predict_datapoint():
#     if request.method=='GET':
#         return render_template('home.html')
#     else:
#         data=CustomData(
#             gender=request.form.get('gender'),
#             race_ethnicity=request.form.get('ethnicity'),
#             parental_level_of_education=request.form.get('parental_level_of_education'),
#             lunch=request.form.get('lunch'),
#             test_preparation_course=request.form.get('test_preparation_course'),
#             reading_score=float(request.form.get('writing_score')),
#             writing_score=float(request.form.get('reading_score'))

#         )
#         pred_df=data.get_data_as_data_frame()
#         print(pred_df)
#         print("Before Prediction")

#         predict_pipeline=PredictPipeline()
#         print("Mid Prediction")
#         results=predict_pipeline.predict(pred_df)
#         print("after Prediction")
#         return render_template('home.html',results=results[0])
    

# if __name__=="__main__":
#     app.run(host="0.0.0.0")  

# #  app.run(host="0.0.0.0",debug=True) # while deploying we have to make sure debug is false
# # Note: The debug mode is set to True for development purposes. It should be set to False in production to avoid exposing sensitive information and to improve performance.

# # This code is part of a Flask application that serves a machine learning model for predicting student performance based on various features.
# # It includes routes for rendering the home page and processing user input to make predictions.
# # The application uses a custom data class to handle input data and a prediction pipeline to generate results.
# # The application is designed to run on a local server and can be accessed via a web browser.
# # The code is structured to handle both GET and POST requests, allowing users to submit data through a form and receive predictions in response.
# # The application uses Flask's rendering capabilities to display HTML templates and return results to the user.
# # The application is set to run in debug mode, which is useful for development and testing purposes.
# # The code imports necessary libraries such as Flask, NumPy, Pandas, and scikit-learn for data processing and machine learning tasks.
# # The application is designed to be modular, with separate files for data processing and prediction logic, promoting code organization and maintainability.

