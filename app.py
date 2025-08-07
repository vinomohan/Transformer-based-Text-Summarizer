# app.py
import streamlit as st

from summarizers.abstractive import generate_abstractive_summary
from summarizers.extractive import generate_extractive_summary
from utils.pdf_parser import extract_text_from_pdf
from utils.url_fetcher import fetch_article_text

st.set_page_config(page_title="Smart Document Summarizer", layout="wide")

st.markdown("""
    <style>
    html, body, [class*="css"]  {
        font-family: 'Segoe UI', sans-serif;
        background-color: #ffffff !important;
        color: #222222;
    }
    .stButton > button {
        background: linear-gradient(90deg, #1d976c, #93f9b9);
        color: white;
        border: none;
        padding: 10px 20px;
        font-size: 16px;
        border-radius: 8px;
        font-weight: bold;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }
    .stTextArea, .stTextInput, .stSelectbox, .stFileUploader, .stSlider {
        background-color: #f9f9f9;
        border-radius: 10px;
        padding: 1rem;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
    }
    .summary-card {
        background: linear-gradient(to right, #fdfdfd, #eef5f9);
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div style="text-align:center; padding: 1rem;">
        <h1 style="font-size: 3rem; color: #0d3b66;">🧠 Smart Document Summarizer</h1>
        <p style="font-size: 1.1rem; color: #333; max-width: 750px; margin: 0 auto;">
            Upload a document, paste text, or enter a URL and get clean, concise AI-powered summaries using modern NLP models.
        </p>
    </div>
""", unsafe_allow_html=True)

input_type = st.radio("Choose Input Type:", ["Upload PDF", "Paste Text", "Enter URL"], horizontal=True)
text_data = ""

if input_type == "Upload PDF":
    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
    if uploaded_file:
        text_data = extract_text_from_pdf(uploaded_file)
elif input_type == "Paste Text":
    text_data = st.text_area("Paste your document text here")
elif input_type == "Enter URL":
    url = st.text_input("Enter Article URL")
    if url:
        text_data = fetch_article_text(url)

if text_data:
    st.markdown(f"<h4 style='color:#1d3557;'>📄 Input Length: {len(text_data.split())} words</h4>", unsafe_allow_html=True)
    summary_type = st.radio("Choose Summary Type:", ["Extractive", "Abstractive"], horizontal=True)
    num_sentences = 5
    if summary_type == "Extractive":
        num_sentences = st.slider("Number of sentences (for extractive summary):", 3, 10, 5)

    if st.button("🚀 Generate Summary"):
        with st.spinner("Summarizing..."):
            if summary_type == "Extractive":
                summary = generate_extractive_summary(text_data, num_sentences=num_sentences)
            else:
                summary = generate_abstractive_summary(text_data)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<div class='summary-card'><h3 style='color:#0d3b66;'>📄 Original Document</h3>", unsafe_allow_html=True)
            st.text_area("Original Document", text_data, height=300)
            st.markdown("</div>", unsafe_allow_html=True)
        with col2:
            st.markdown("<div class='summary-card'><h3 style='color:#0d3b66;'>📝 AI Summary</h3>", unsafe_allow_html=True)
            st.text_area("Summary Output", summary, height=300)
            st.markdown(f"<p style='color:#555;'>📏 Summary Length: {len(summary.split())} words</p>", unsafe_allow_html=True)
            st.download_button("📥 Download Summary", summary, file_name="summary.txt")
            st.markdown("</div>", unsafe_allow_html=True)
