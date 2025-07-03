import streamlit as st
from transformers import pipeline
from PyPDF2 import PdfReader

# Load HuggingFace summarizer pipeline
from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6",  # or another model if preferred
    tokenizer="sshleifer/distilbart-cnn-12-6",
    device=0 # -1 for CPU, or 0 if you're using GPU
)


# Streamlit app configuration
st.set_page_config(page_title=" TEXT SUMMARIZATION", layout="centered")
st.title("📄  TEXT SUMMARIZATION")
st.markdown("Upload a text or PDF document — we'll extract and summarize it using AI!")

# Upload file (no image support)
uploaded_file = st.file_uploader("📂 Upload a document (.pdf, .txt)", type=["txt", "pdf"])

extracted_text = ""

# Handle uploaded file
if uploaded_file:
    file_type = uploaded_file.type
    st.success(f"✅ Uploaded: `{uploaded_file.name}`")
    st.write("📄 Detected file type:", file_type)

    # Text file
    if file_type == "text/plain":
        extracted_text = uploaded_file.read().decode("utf-8")

    # PDF file
    elif file_type == "application/pdf":
        pdf_reader = PdfReader(uploaded_file)
        for page in pdf_reader.pages:
            extracted_text += page.extract_text() or ""

    else:
        st.warning("⚠️ Unsupported file type.")

# Show extracted text
user_text = st.text_area("✏️ Extracted or pasted text:", value=extracted_text, height=300)

# Word and character stats
if user_text.strip():
    st.info(f"🧾 Word Count: {len(user_text.split())} | Character Count: {len(user_text)}")

# Summarization logic
if st.button("📄 Summarize"):
    if user_text.strip() == "":
        st.warning("⚠️ Please upload or enter some text.")
    else:
        with st.spinner("🔄 Summarizing..."):
            summary = summarizer(user_text, max_length=130, min_length=30, do_sample=False)[0]['summary_text']
            st.success("✅ Summary:")
            st.write(summary)

            # Download summary
            st.download_button("📥 Download Summary as TXT", summary, file_name="summary.txt")
