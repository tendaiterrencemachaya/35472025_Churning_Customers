from flask import Flask, render_template, request
import joblib
import scipy.stats as stats
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Loading my optimized churn model
model = joblib.load('optimized0_churn_model.joblib')

# Loading scaler that was used during training
scaler = joblib.load('churn0_standard_scaler.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Getting user input from the HTML form
        feature1 = float(request.form['Total_Charges'])
        feature2 = float(request.form['tenure'])
        feature3 = float(request.form['monthlyCharges'])
        feature4 = float(request.form['Contract_Month-to-month'])
        feature5 = float(request.form['OnlineSecurity_No'])
        feature6 = float(request.form['PaymentMethod_Electronic check'])
        feature7 = float(request.form['TechSupport_No'])

        # Creating a user input list
        user_inputs = [[feature1, feature2, feature3, feature4, feature5, feature6, feature7]]

        # Applying the same scaling as used during training
        user_inputs_scaled = scaler.transform(user_inputs)

        # Making predictions using the model
        prediction = model.predict(user_inputs_scaled)[0]

        # Setting a threshold of 0.5 for classification
        if prediction >= 0.5:
            churn_result = "Yes" # You might need to customize the confidence interval calculation based on your model
        # Example below is a placeholder, you might need to adapt it based on your model's characteristics
        else:
            churn_result = "No"

        std_error = 0.2922120988368988  # from your model testing
        margin_of_error = std_error * stats.t.ppf((1 + 0.95) / 2, 7043 - 1)  # 95% confidence interval

        # Assuming `prediction` is the predicted probability
        lower_bound = max(0, prediction[0] - margin_of_error)
        upper_bound = min(1, prediction[0] + margin_of_error)

        # Calculate the width of the confidence interval
        confidence_factor = upper_bound - lower_bound

        # 84% CONFIDENCE LEVEL
        confidence_level = 95

        # Displaying the prediction, confidence factor, and confidence level on the web page
        return render_template('index.html', prediction=churn_result, confidence_factor=round(confidence_factor, 2)*100, confidence_level=confidence_level)

if __name__ == '__main__':
    app.run(debug=True)
