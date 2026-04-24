import streamlit as st
import joblib

vectorizer = joblib.load("vectorizer.jb")
model = joblib.load("lr_model.jb")
st.title("Fake News Detector")
st.write("Enter the news text below to check if it's real or fake.")

news_input = st.text_area("News Article: ","")

if st.button("Check News"):
    if news_input.strip() :
        transformed_input = vectorizer.transform([news_input])
        prediction = model.predict(transformed_input)[0]
        if prediction == 1:
            st.success("This news is Real! ")
        else:
            st.error("This news is Fake! ")
    else:
        st.warning("Please enter some news text to check.")        
