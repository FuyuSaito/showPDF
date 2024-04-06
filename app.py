# PDFを入力して、その中のテキストを表示する。
# ただし、表示するテキストの行数は、スライダーバーで調整できるようにする

import streamlit as st
import pdfplumber

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text.strip() + "\n"  # 改行を追加
        return text

def main():
    st.title("PDF Text Extractor")
    
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    
    if uploaded_file is not None:
        text = extract_text_from_pdf(uploaded_file)
        
        st.sidebar.subheader("Number of Sentences to Display")
        
        if text.count("。") == 0:  # 読み込んだ文章が1行の場合
            st.sidebar.write("読み込んだ文章数は1分のみでした。")
        else:
            max_sentences = text.count("。")  # "。"の数をカウント
            num_sentences = st.sidebar.slider("Select the number of sentences to display", 1, max_sentences, max_sentences)
            
            sentences = text.split("。")
            extracted_sentences = []
            for s in sentences:
                s = s.strip()
                if s:  # 空の文を削除
                    if s[-1] == "。":  # 文の終わりが句点で終わっている場合
                        extracted_sentences.append(s)
                    else:
                        extracted_sentences.append(s + "。")
            
            st.subheader("Extracted Text")
            for sentence in extracted_sentences[:num_sentences]:
                st.write(sentence)

if __name__ == "__main__":
    main()
