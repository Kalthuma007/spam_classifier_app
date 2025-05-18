# 🚫 Spam Classifier Web App

This project is a simple machine learning-based web application that classifies input messages as **Spam** or **Not Spam** using a trained model. The app is built using **Flask** and **scikit-learn**, and it has a user-friendly front-end.

## 📌 Features

- Machine Learning model trained using TF-IDF and Naive Bayes
- Web interface built with Flask
- Clean and simple UI using HTML/CSS
- Can be easily deployed on platforms like Render or Railway

## 🧠 Tech Stack

- Python
- scikit-learn
- pandas
- Flask
- HTML/CSS

## 🗂️ Project Structure

```
.
├── app.py
├── spam_classifier.py
├── model.pkl
├── notebook.ipynb
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
├── static/
│   └── style.css
```

## 🚀 How to Run Locally

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/spam-classifier.git
cd spam-classifier
```

2. **Create a virtual environment (optional but recommended)**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the app**

```bash
python app.py
```

5. **Visit in your browser**  
[http://127.0.0.1:5000](http://127.0.0.1:5000)

## ✨ Screenshot

_Add a screenshot of your app here if you like._

## 📜 License

This project is open source and available under the [MIT License](LICENSE).
