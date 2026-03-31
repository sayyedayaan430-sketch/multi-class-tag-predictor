Multi-Class Tag Predictor
�
￼ ￼ ￼ ￼ ￼ 


�
An intelligent multi-label tag prediction system that automatically assigns relevant tags to text using NLP and Machine Learning. 


📌 Table of Contents
Overview
Demo
Features
Project Structure
Tech Stack
Getting Started
How It Works
Model Performance
Dataset
Contributing
License
🔍 Overview
Given a piece of text (such as a Stack Overflow question or article), this system predicts one or more relevant tags from a large predefined set using TF-IDF vectorization and OneVsRest Logistic Regression.
Example:
Input  : "How do I merge two DataFrames in pandas using a common column?"
Output : ['python', 'pandas', 'dataframe', 'merge']
🎥 Demo
🚀 Run the Streamlit app locally to see it in action!
streamlit run app.py
✨ Features
✅ Multi-label tag prediction (a single input can get multiple tags)
✅ Clean and interactive Streamlit web interface
✅ Text preprocessing pipeline (cleaning, stopword removal, lemmatization)
✅ TF-IDF feature extraction with bigram support
✅ Confidence scores displayed per predicted tag
✅ Model serialization — train once, predict anytime
✅ Modular and well-commented codebase
