# 🚀 Transformer-based Text Summarizer

An intelligent and interactive document summarization tool powered by transformer-based NLP models. This Streamlit-based web app supports extractive and abstractive summarization from PDF uploads, raw text, or URLs.

> 🔍 Built for researchers, professionals, and learners to generate clean, concise summaries using modern NLP techniques like Sentence-BERT and T5.

---

## 🧠 Features

- 📄 **Input Options**: Upload PDF, paste text, or enter a web URL
- 🧾 **Extractive Summary**: Using Sentence-BERT and cosine similarity
- ✨ **Abstractive Summary**: Using pretrained Transformer models (e.g., T5)
- 📊 **Input Stats**: Word count and summary length
- 💾 **Downloadable Output**: Save the generated summary as `.txt`
- 🧱 **Responsive UI**: Clean layout with cards, gradient backgrounds, and modern theme

---

**How It Works
**
🔹 Extractive Summarization
Uses Sentence-BERT embeddings
Computes cosine similarity matrix between sentences
Selects top-N representative sentences (optionally boosted for named entities)

🔹 Abstractive Summarization
Utilizes pretrained models like T5
Converts text to a summarized version by generating new content
Ideal for large documents and semantic understanding|
