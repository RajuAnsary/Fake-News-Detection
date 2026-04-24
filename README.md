# 📰 Fake News Detection using Machine Learning

A machine learning-based web application that classifies news articles as **Real** or **Fake** using **Natural Language Processing (NLP)** and **Logistic Regression**.

## 🚀 Live Demo
👉 https://fake-news-detector801.streamlit.app/

---

## 📌 Overview
This project detects misinformation by analyzing news article text and predicting whether it is fake or real.

It uses:
- Text preprocessing
- TF-IDF vectorization
- Logistic Regression classifier
- Streamlit deployment

---

## ✨ Features
- Detect fake and real news articles
- User-friendly Streamlit interface
- NLP preprocessing pipeline
- TF-IDF feature extraction
- Logistic Regression classification
- Real-time prediction from user input

---

## 🛠 Tech Stack
- Python
- Pandas
- Scikit-learn
- Streamlit
- Joblib
- NLP / TF-IDF

---

## 📂 Dataset
Dataset used:

**Fake and Real News Dataset** (Kaggle)

Contains:
- Fake news articles
- Real news articles

Labels:
- `1` → Fake News  
- `0` → Real News

---

## 🔄 Workflow

1. Data Collection  
2. Data Preprocessing  
3. Exploratory Data Analysis  
4. Train-Test Split  
5. TF-IDF Vectorization  
6. Logistic Regression Model Training  
7. Model Evaluation  
8. Streamlit Deployment  

---

## 🤖 Machine Learning Model
### Logistic Regression
Used because:
- Efficient for text classification
- Works well with sparse TF-IDF vectors
- Fast and interpretable

---

## 📊 Model Performance

Classification Report:

```text
precision    recall    f1-score    support

0      0.99      0.99      0.99      5895
1      0.98      0.99      0.99      5330

accuracy                        0.99    11225
macro avg    0.99      0.99      0.99    11225
weighted avg 0.99      0.99      0.99    11225
```

### Performance Metrics
- Accuracy: **99%**
- Precision: **99%**
- Recall: **99%**
- F1 Score: **99%**

---

## 💻 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/fake-news-detection.git
cd fake-news-detection
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run app:

```bash
streamlit run app.py
```

---

## ▶️ Usage
1. Open the Streamlit app  
2. Paste a news article  
3. Click **Check News**  
4. Get prediction:
- Real News ✅
- Fake News ❌

---

## 📁 Project Structure

```bash
Fake_News_Detection/
│
├── app.py
├── app.ipynb
├── lr_model.jb
├── vectorizer.jb
├── requirements.txt
└── README.md
```

---

## Future Improvements
- Add confidence probability visualization
- Use advanced NLP models (BERT)
- Integrate live fact-checking APIs
- Improve model with newer datasets

---

## Author
**Raju Ansary**
