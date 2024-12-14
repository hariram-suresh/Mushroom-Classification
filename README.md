# Mushroom-Classification
iNeuron project regarding classification of mushroom(whether edible or not) based its features

# Mushroom Edibility Prediction with Web Application

## **Project Overview**

This project predicts whether a mushroom is **edible** or **poisonous** based on its physical characteristics using a machine learning model. The dataset comes from the Audubon Society Field Guide to North American Mushrooms and contains descriptions of gilled mushrooms in the Agaricus and Lepiota family. The project also includes a web application to interactively classify mushrooms using the trained model.

---

## **Problem Statement**

The main goal of this project is to predict whether a mushroom is edible or poisonous based on its attributes. The problem statement highlights:

- Mushrooms are categorized as:

  - **Definitely edible**
  - **Definitely poisonous**
  - **Maybe edible but not recommended** (merged with the poisonous category for simplicity).

- The dataset contains 23 species and multiple categorical features describing physical attributes such as cap shape, odor, gill size, etc.

---

## **Approach**

### **1. Data Pipeline**

- **Data Exploration**: Performed exploratory data analysis (EDA) to understand the data distribution, visualize patterns, and detect anomalies.
- **Data Cleaning**: Addressed missing values and standardized categorical values.
- **Feature Engineering**: Applied encoding techniques (label encoding) to convert categorical features into numeric format.
- **Data Splitting**: Split the dataset into training and testing sets (e.g., 70-30 split).

### **2. Model Development**

- Tested a machine learning algorithm:

  - Decision Tree

- Selected the model with the best performance based on:

  - Accuracy
  - F1-Score

### **3. Model Evaluation**

- Used metrics such as confusion matrix and cross-validation to evaluate model performance.

### **4. Web Application**

- Built a user-friendly web application using **Streamlit**:
  - Allows users to input mushroom features.
  - Predicts and displays whether the mushroom is edible or poisonous.

---

## **Tech Stack**

### **Programming Language:**

- Python

### **Libraries Used:**

- **Data Processing**: pandas, numpy, pickle, joblib
- **Visualization**: klib, seaborn
- **Machine Learning**: scikit-learn
- **Web Framework**: Streamlit

---

## **Installation and Usage**

### **Prerequisites**

- Python 3.8 or above
- pip package manager

### **Steps to Run the Project Locally**

1. Clone the Repository:

   ```bash
   git clone https://github.com/yourusername/mushroom-prediction-webapp.git
   cd mushroom-prediction-webapp
