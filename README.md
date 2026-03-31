# 🏷️ Multi-Class Tag Predictor

  An intelligent multi-label tag prediction system that automatically assigns relevant tags to text using NLP and Machine Learning.


---

## 📌 Table of Contents

- [Overview](#-overview)
- [Demo](#-demo)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-getting-started)
- [How It Works](#-how-it-works)
- [Model Performance](#-model-performance)
- [Dataset](#-dataset)
- [How to Run](#-how-to-run)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🔍 Overview

Given a piece of text (such as a Stack Overflow question or article), this system predicts one or more relevant tags from a large predefined set using **TF-IDF vectorization** and **OneVsRest Logistic Regression**.

**Example:**
```
Input  : "How do I merge two DataFrames in pandas using a common column?"
Output : ['python', 'pandas', 'dataframe', 'merge']
```

---

## 🎥 Demo

> 🚀 Run the Streamlit app locally to see it in action!

```bash
streamlit run app.py
```

---

## ✨ Features

- ✅ Multi-label tag prediction (a single input can get multiple tags)
- ✅ Clean and interactive **Streamlit** web interface
- ✅ Text preprocessing pipeline (cleaning, stopword removal, lemmatization)
- ✅ TF-IDF feature extraction with bigram support
- ✅ Confidence scores displayed per predicted tag
- ✅ Model serialization — train once, predict anytime
- ✅ Modular and well-commented codebase

---

## 🗂️ Project Structure

```
multi-class-tag-predictor/
│
├── 📁 data/
│   ├── raw/                        # Original downloaded dataset
│   └── processed/                  # Cleaned & preprocessed data
│
├── 📁 models/                      # Saved model artifacts (.pkl)
│   ├── tag_model.pkl
│   ├── tfidf.pkl
│   └── mlb.pkl
│
├── 📁 notebooks/
│   └── exploration.ipynb           # EDA, experiments, visualizations
│
├── 📁 src/
│   ├── preprocess.py               # Text cleaning & feature engineering
│   ├── train.py                    # Model training pipeline
│   ├── predict.py                  # Prediction logic
│   └── evaluate.py                 # Metrics & evaluation report
│
├── 📁 assets/
│   └── screenshot.png              # App screenshot for README
│
├── app.py                          # Streamlit web application
├── requirements.txt                # Python dependencies
├── .gitignore                      # Files to exclude from Git
└── README.md                       # Project documentation
```

---

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| **Language** | Python 3.9+ |
| **ML / NLP** | scikit-learn, NLTK |
| **Web App** | Streamlit |
| **Data** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn |
| **Serialization** | Pickle |

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/multi-class-tag-predictor.git
cd multi-class-tag-predictor
```

### 2. Create a Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Download NLTK Resources
```python
python -c "import nltk; nltk.download('stopwords'); nltk.download('wordnet')"
```

### 5. Add Your Dataset
Place your CSV file inside `data/raw/`. It must contain:
- `text` column — the question or article body
- `tags` column — space or comma-separated tags

### 6. Train the Model
```bash
python src/train.py
```

### 7. Launch the Web App
```bash
streamlit run app.py
```

---

## ⚙️ How It Works

```
Raw Text
   │
   ▼
┌─────────────────────────┐
│   Text Preprocessing    │  → Lowercase, remove punctuation,
│   (preprocess.py)       │    stopwords, lemmatization
└─────────────────────────┘
   │
   ▼
┌─────────────────────────┐
│   TF-IDF Vectorizer     │  → Convert text to numerical features
│   (max 50k features)    │    using unigrams + bigrams
└─────────────────────────┘
   │
   ▼
┌─────────────────────────┐
│  OneVsRest Classifier   │  → One Logistic Regression model
│  (Logistic Regression)  │    trained per tag
└─────────────────────────┘
   │
   ▼
Predicted Tags with Confidence Scores
```

---

## 📊 Model Performance

| Metric | Score |
|---|---|
| F1 Score (micro) | ~0.78 |
| F1 Score (macro) | ~0.61 |
| Hamming Loss | ~0.009 |

> ⚠️ Scores are approximate and depend on the dataset used.

---

## 📁 Dataset

Recommended datasets to get started:

| Dataset | Source | Description |
|---|---|---|
| Stack Overflow Questions | [Kaggle](https://www.kaggle.com/) | Questions with tech tags |
| Research Paper Abstracts | [arXiv](https://arxiv.org/) | Papers with topic labels |
| Toxic Comment Dataset | [Kaggle](https://www.kaggle.com/) | Multi-label text dataset |

Search **"Stack Overflow questions tags"** on Kaggle for the best beginner dataset.

---

## ▶️ How to Run

> Make sure you have completed all steps in **Getting Started** above first.

**Step 1 — Train the model** *(only once)*
```bash
python src/train.py
```

**Step 2 — Launch the web app**
```bash
streamlit run app.py
```

**Step 3 — Open in browser**
```
http://localhost:8501
```

**Step 4 — Type any text and click "Predict Tags"** 🎉

> 💡 Or run predictions directly from terminal:
> ```bash
> python src/predict.py --text "How do I sort a list in Python?"
> ```

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<p align="center">Made with ❤️ using Python & Streamlit</p>
