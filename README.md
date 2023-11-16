# Churn Prediction Application fused with a Neural Networks Customer Churn Prediction model 

## Overview:
This project aims to predict customer churn in a telecommunications company using neural networks. Customer churn, or customer attrition, refers to the phenomenon where customers stop doing business with a company. Predicting customer churn is essential for businesses to implement targeted retention strategies and minimize revenue loss.

## Table of Contents

    Introduction
    Dataset
    Model Training
    Model Evaluation
    Best Model Selection
    Optimized Model
    Technologies Used
    Functionality
    Demo Video
    How to Run
    Conclusion
    Contributors

## Introduction

- Customer churn prediction involves building machine learning models to identify customers who are likely to leave the service. In this project, we employ neural networks, a subset of machine learning, to predict customer churn based on historical data.

## Dataset

- The dataset used for this project contains various features related to customer behavior, such as usage patterns, contract details, and customer feedback. The target variable is binary, indicating whether a customer has churned (1) or not (0).

## Model Training

- We train multiple neural network models with different hyperparameter configurations to find the optimal set of parameters. The training is performed on a training set, and model performance is evaluated on a validation set. The hyperparameters include the number of units in each layer, dropout rates, and the optimizer.

## Model Evaluation

- The trained models are evaluated using the test set, and performance metrics such as accuracy and area under the receiver operating characteristic curve (AUC-ROC) are computed. These metrics provide insights into how well the models generalize to unseen data.
  
## Best Model Selection

- We use grid search with cross-validation to find the best hyperparameters for our neural network. The model with the highest validation performance is selected as the best model. The evaluation metrics for this model on the test set are reported.

## Optimized Model

- An optimized neural network model is created based on the best hyperparameters. This model is then trained and evaluated to assess its performance. The goal is to further fine-tune the model and achieve better results.

## Technologies Used:
1. Python

    Description: Python serves as the primary programming language for the development of the churn machine learning model, data preprocessing, and analysis.

2. Machine Learning Libraries
a. TensorFlow and Keras

    Description: TensorFlow is employed as the deep learning framework, and Keras, integrated with TensorFlow, is used to build and train neural network models.

b. Scikit-learn

    Description: Scikit-learn is utilized for various machine learning tasks, including data preprocessing, model evaluation, and hyperparameter tuning.

3. Data Analysis and Visualization
a. Pandas

   Description: Pandas is used for data manipulation and analysis, particularly for handling the dataset.

b. Matplotlib and Seaborn

    Description: Matplotlib and Seaborn are used for data visualization to gain insights into the dataset and the model performance.

4. Jupyter Notebooks

    Description: Google Colab Notebooks are employed for an interactive and collaborative development environment. The code for this project is organized and presented in google colab Notebooks to enhance readability and understanding.

5. Version Control

    Description: Git is used for version control, enabling collaborative development and tracking changes to the codebase.

7. Documentation

    Description: Markdown is used for creating documentation, including this README file, to provide an overview of the project and guide users on how to explore and use the code.
   
8. Web Framework: Flask
9. Frontend: HTML, CSS

## Functionality:
- Users can input customer data via a web interface.
- The application sends the data to the deployed model for prediction.
- The prediction (churn or not) and confidence factor are displayed on the interface.

## Demo Video:
[Watch the Demo Video](https://drive.google.com/file/d/1ri21VikiOq0rqxoD1TSPHiO-8LB69IDb/view?usp=drive_link)

## How to Run:
1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Run the application using `python app.py`.
4. Access the application at `http://localhost:5000` in your web browser.


## Conclusion

- The project concludes with insights into the predictive capabilities of the neural network models and recommendations for leveraging the results to implement targeted customer retention strategies.

## Contributors:
-  Tendai Terrence Machaya
  






