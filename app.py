import streamlit as st
import pickle
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier 

# Create a function that load your pickle model
def load_model():
    ### Begining of your code ###
    model = None
    ### End of your code ###
    return model

# Create a function that return the label and the color of the prediction
# 1 -> A in Green
# 2 -> B in Light Green
# 3 -> C in Yellow
# 4 -> D in Orange
# 5 -> E in Orange-Red
# 6 -> F in Red
# 7 -> G in Dark Red
def get_color_label(prediction):

    ### Beginin of your code ###
    labels = {
        1: None,        # Green
        2: None,        # Light Green
        3: None,        # Yellow
        4: None,        # Orange
        5: None,        # Orange-Red
        6: None,        # Red
        7: None,        # Dark Red
    }
    ### End of your code ###

    return labels.get(prediction, ("Unknown", "#FFFFFF"))

# Load model using the function load_model()
### Your code ###
model = None
### Your code ###

# Give a title at your page using st.title
### Your code ###
None
### Your code ###

# Define input fields with all the features of yoru model 
### Your code ###
feature_names = [None]
### Your code ###

user_input = {}
for feature in feature_names:
    # Create a number input for each feature
    ### Your code ###
    user_input[feature] = None
    ### You code ###

if st.button("Predict"):
    ### Your code ###
    # Create an array with the user input
    input_array = None

    # Make a prediction using the model using input_array
    prediction = None

    # Get the label and the color of the prediction
    label, color = None
    ### Your code ###
    
    st.markdown(f"""<h1 style='color:{color}; text-align:center;'>{label}</h1>""", unsafe_allow_html=True)
   