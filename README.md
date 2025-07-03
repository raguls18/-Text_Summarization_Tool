# 📝 Text Summarization Tool

A smart and interactive tool that summarizes long articles, documents, or images using state-of-the-art Natural Language Processing (NLP) models. Built with **Streamlit**, this app supports text, PDF, and image uploads (with OCR), and generates concise, human-readable summaries.

---

## ✨ Features

- ✅ Summarize long paragraphs, articles, or documents
- 📂 Upload support for `.txt`, `.pdf`, and image files (`.png`, `.jpg`)
- 🔍 OCR support using Tesseract for text extraction from images
- 🧠 Summarization using Hugging Face's `distilbart-cnn-12-6` model
- 📊 Word and character count display
- 💾 Download the summary as a `.txt` file
- ⚡ Clean and responsive Streamlit UI

---

## 📦 Dependencies

Install the required libraries:

```bash
pip install streamlit transformers PyPDF2 pytesseract pillow
