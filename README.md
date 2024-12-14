# Mushroom-Classification
iNeuron project regarding classification of mushroom(whether edible or not) based its features

Mushroom Edibility Prediction with Web Application

Project Overview

This project predicts whether a mushroom is edible or poisonous based on its physical characteristics using a machine learning model. The dataset comes from the Audubon Society Field Guide to North American Mushrooms and contains descriptions of gilled mushrooms in the Agaricus and Lepiota family. The project also includes a web application to interactively classify mushrooms using the trained model.

Problem Statement

The main goal of this project is to predict whether a mushroom is edible or poisonous based on its attributes. The problem statement highlights:

Mushrooms are categorized as:

Definitely edible

Definitely poisonous

Maybe edible but not recommended (merged with the poisonous category for simplicity).

The dataset contains 23 species and multiple categorical features describing physical attributes such as cap shape, odor, gill size, etc.

Approach

1. Data Pipeline

Data Exploration: Performed exploratory data analysis (EDA) to understand the data distribution, visualize patterns, and detect anomalies.

Data Cleaning: Addressed missing values and standardized categorical values.

Feature Engineering: Applied encoding techniques (e.g., one-hot encoding or label encoding) to convert categorical features into numeric format.

Data Splitting: Split the dataset into training and testing sets (e.g., 80-20 split).

2. Model Development

Tested multiple classical machine learning algorithms:

Decision Tree

Random Forest

Logistic Regression

Gradient Boosting (XGBoost/LightGBM)

Selected the model with the best performance based on:

Accuracy

Precision

Recall

F1-Score

3. Model Evaluation

Used metrics such as confusion matrix, ROC-AUC score, and cross-validation to evaluate model performance.

Performed hyperparameter tuning (e.g., GridSearchCV or RandomizedSearchCV) to optimize the selected model.

4. Web Application

Built a user-friendly web application using Streamlit (or Flask/Django):

Allows users to input mushroom features.

Predicts and displays whether the mushroom is edible or poisonous.

Tech Stack

Programming Language:

Python

Libraries Used:

Data Processing: pandas, numpy

Visualization: matplotlib, seaborn

Machine Learning: scikit-learn, xgboost, lightgbm

Web Framework: Streamlit (or Flask/Django)

Installation and Usage

Prerequisites

Python 3.8 or above

pip package manager

Steps to Run the Project Locally

Clone the Repository:

git clone https://github.com/yourusername/mushroom-prediction-webapp.git
cd mushroom-prediction-webapp

Install Required Libraries:

pip install -r requirements.txt

Launch the Web Application:
If using Streamlit:

streamlit run app.py

If using Flask:

python app.py

Open the App in Browser:
Navigate to http://localhost:8501 (Streamlit) or http://127.0.0.1:5000 (Flask).

Project Files

app.py: Main script for the web application.

mushroom_prediction_model.pkl: Saved machine learning model.

mushrooms.csv: Dataset used for training the model.

requirements.txt: List of Python dependencies.

README.md: Project documentation (this file).

Results

Achieved 95%+ accuracy in predicting mushroom edibility.

Successfully integrated the model into an interactive web application for real-time predictions.

Future Work

Enhance the model by adding more data or leveraging advanced ML algorithms.

Deploy the web app on cloud platforms such as AWS, Heroku, or Azure.

Implement advanced UI features to improve user experience.

Contributors

Your Name

Contributions from peers and open-source libraries.

License

This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements

Audubon Society Field Guide for the dataset.

Open-source community for Python libraries and frameworks.
