"""
app.py
──────
Streamlit web application for the Multi-Class Tag Predictor.

Run with:
    streamlit run app.py
"""

import streamlit as st
import os
import sys

# Add src/ to the Python path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# ─── Page Configuration ────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Multi-Class Tag Predictor",
    page_icon="🏷️",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ─── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    /* Main background */
    .stApp { background-color: #0f1117; }

    /* Title styling */
    h1 { color: #ffffff; font-size: 2.2rem !important; }
    h3 { color: #c9d1d9; }

    /* Tag badge styling */
    .tag-badge {
        display: inline-block;
        background: linear-gradient(135deg, #238636, #2ea043);
        color: white;
        padding: 6px 14px;
        border-radius: 20px;
        margin: 5px 4px;
        font-size: 0.9rem;
        font-weight: 600;
        letter-spacing: 0.4px;
    }

    /* Confidence card */
    .conf-card {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 10px;
        padding: 12px 18px;
        margin: 6px 0;
    }

    /* Text area styling */
    .stTextArea textarea {
        background-color: #161b22 !important;
        color: #c9d1d9 !important;
        border: 1px solid #30363d !important;
        border-radius: 8px !important;
        font-size: 1rem !important;
    }

    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #238636, #2ea043);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 28px;
        font-size: 1rem;
        font-weight: 600;
        width: 100%;
        cursor: pointer;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #161b22;
        border-right: 1px solid #30363d;
    }

    /* Metric cards */
    div[data-testid="metric-container"] {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 8px;
        padding: 12px;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #6e7681;
        font-size: 0.8rem;
        margin-top: 40px;
        padding-top: 20px;
        border-top: 1px solid #30363d;
    }
</style>
""", unsafe_allow_html=True)


# ─── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## ⚙️ Settings")
    st.markdown("---")

    top_n = st.slider(
        "Max tags to return",
        min_value=1, max_value=10, value=5,
        help="Maximum number of predicted tags to display"
    )

    threshold = st.slider(
        "Confidence threshold",
        min_value=0.05, max_value=0.50, value=0.15, step=0.05,
        help="Only show tags with confidence above this value"
    )

    st.markdown("---")
    st.markdown("### 📖 About")
    st.markdown("""
    This app predicts relevant tags for any text using:
    - **TF-IDF** feature extraction
    - **OneVsRest** Logistic Regression
    - **NLTK** text preprocessing
    """)

    st.markdown("---")
    st.markdown("### 📦 Model Info")
    st.info("Train the model first by running `python src/train.py`")


# ─── Main Page ─────────────────────────────────────────────────────────────────
st.markdown("# 🏷️ Multi-Class Tag Predictor")
st.markdown("##### Automatically predict relevant tags for any text using NLP & Machine Learning")
st.markdown("---")

# Example questions for inspiration
EXAMPLES = [
    "How do I merge two DataFrames in pandas using a common column?",
    "What is the difference between a list and a tuple in Python?",
    "How to implement a binary search tree in Java?",
    "Explain how gradient descent works in machine learning",
    "How to handle missing values in a dataset?",
]

st.markdown("### 💬 Enter Your Text")

# Example selector
selected_example = st.selectbox(
    "Or try an example:",
    ["— Choose an example —"] + EXAMPLES,
    label_visibility="collapsed"
)

# Text input area
default_text = "" if selected_example == "— Choose an example —" else selected_example
user_text = st.text_area(
    "Input text",
    value=default_text,
    placeholder="Paste a question, article, or any text here...",
    height=140,
    label_visibility="collapsed"
)

# Predict button
predict_clicked = st.button("🔍 Predict Tags", use_container_width=True)

# ─── Prediction ────────────────────────────────────────────────────────────────
if predict_clicked:
    if not user_text.strip():
        st.warning("⚠️ Please enter some text before predicting.")
    else:
        # Try to load model and predict
        try:
            from predict import predict_tags

            with st.spinner("Analyzing text and predicting tags..."):
                results = predict_tags(user_text, top_n=top_n, threshold=threshold)

            st.markdown("---")

            if not results:
                st.info("No tags predicted above the confidence threshold. Try lowering the threshold in the sidebar.")
            else:
                # Display tag badges
                st.markdown("### 🏷️ Predicted Tags")
                badges_html = " ".join(
                    f'<span class="tag-badge">{r["tag"]}</span>'
                    for r in results
                )
                st.markdown(badges_html, unsafe_allow_html=True)

                st.markdown("---")

                # Display confidence scores
                st.markdown("### 📊 Confidence Scores")
                for r in results:
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.progress(r['confidence'])
                    with col2:
                        st.markdown(f"**{r['tag']}** — `{r['confidence']:.1%}`")

                # Summary metrics
                st.markdown("---")
                col1, col2, col3 = st.columns(3)
                col1.metric("Tags Found", len(results))
                col2.metric("Top Tag", results[0]['tag'])
                col3.metric("Top Confidence", f"{results[0]['confidence']:.1%}")

        except FileNotFoundError as e:
            st.error(f"⚠️ Model not found! Please run `python src/train.py` first.\n\n`{e}`")
        except Exception as e:
            st.error(f"An error occurred: {e}")

# ─── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    Built with ❤️ using Python, scikit-learn & Streamlit
</div>
""", unsafe_allow_html=True)
              
