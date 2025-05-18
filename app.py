from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

# Load your trained model and vectorizer
model = joblib.load('spam_classifier.pkl')
vectorizer = joblib.load('vectorizer.pkl')

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = ""
    if request.method == 'POST':
        message = request.form['message']
        message_vec = vectorizer.transform([message])
        pred = model.predict(message_vec)[0]
        prediction = f"This message is: {pred.upper()}"
    return render_template('index.html', prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
