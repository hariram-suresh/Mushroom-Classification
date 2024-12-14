import streamlit as st
import pandas as pd
import joblib
import logging
from sklearn.preprocessing import LabelEncoder

logging.basicConfig(filename="user_access.log", level=logging.INFO, format="%(asctime)s - %(message)s")

model = joblib.load("model.pkl")

file_path = "mushrooms_data_detailed.csv"
mushrooms_data = pd.read_csv(file_path)
X = mushrooms_data.drop(columns=["class","odor"])

label_encoders = {col: LabelEncoder().fit(mushrooms_data[col]) for col in mushrooms_data.columns}

USERS = {"admin": "Hari", "user": "password"}

if "is_logged_in" not in st.session_state:
    st.session_state["is_logged_in"] = False

def login():
    """Authenticate the user."""
    st.sidebar.title("Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    login_button = st.sidebar.button("Login")

    if login_button:
        if username in USERS and USERS[username] == password:
            st.session_state["is_logged_in"] = True  
            st.sidebar.success("Login successful!")
            logging.info(f"User '{username}' logged in.")
            main()
        else:
            st.sidebar.error("Invalid username or password.")
            logging.warning(f"Failed login attempt for username: {username}")

def main():
    st.title("Mushroom Classification")
    st.write("Hey there!, feel free to classify mushrooms as edible or poisonous by selecting features below!")

    inputs = {}
    for feature in X.columns:
        options = mushrooms_data[feature].unique()
        selected_option = st.selectbox(f"Select {feature}:", options)
        inputs[feature] = selected_option

    encoded_inputs = [label_encoders[feature].transform([inputs[feature]])[0] for feature in X.columns]

    st.write("Encoded input shape:", len(encoded_inputs))
    st.write("Model expects:", model.n_features_in_) 

    if st.button("Predict"):
        if len(encoded_inputs) != model.n_features_in_:
            st.error(f"Feature mismatch: Model expects {model.n_features_in_} features, but got {len(encoded_inputs)}.")
        else:
            prediction = model.predict([encoded_inputs])
            result = label_encoders["class"].inverse_transform(prediction)[0]
            st.success(f"The mushroom is predicted to be: **{'Edible' if result == 'e' else 'Poisonous'}**")

if __name__ == "__main__":
    if not st.session_state["is_logged_in"]:
        login()
    else:
        main()
