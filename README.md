# 📄 Career Match AI

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue.svg" />
  <img src="https://img.shields.io/badge/Framework-Streamlit-red.svg" />
  <img src="https://img.shields.io/badge/NLP-TF--IDF-orange.svg" />
  <img src="https://img.shields.io/badge/ML-Scikit--Learn-success.svg" />
  <img src="https://img.shields.io/badge/Deployment-Streamlit%20Cloud-brightgreen.svg" />
</p>

<p align="center">
  🚀 AI-powered Resume & Job Description Matching System using NLP
</p>

---

## 🌐 Live Demo

🔗 **Try the Live App Here:**  
👉 h

---

## 📌 Project Overview

The **AI Resume Job Matcher** is an intelligent NLP-based web application that compares a candidate’s resume with a job description and calculates a similarity score.

It helps:

- 🧑‍💼 Job seekers analyze resume-job fit  
- 🏢 Recruiters screen resumes faster  
- 📊 HR teams improve hiring efficiency  

---

## 🧠 How It Works

1️⃣ Upload Resume (PDF)  
2️⃣ Paste Job Description  
3️⃣ System extracts text from resume  
4️⃣ Applies text preprocessing  
5️⃣ Converts text into TF-IDF vectors  
6️⃣ Calculates cosine similarity  
7️⃣ Displays match percentage  

---

## ⚙️ Tech Stack

- Python
- Streamlit
- Scikit-learn
- TF-IDF Vectorizer
- Cosine Similarity
- PyPDF2 (PDF text extraction)

---

## 📂 Project Structure

```bash
AI-Resume-Job-Matcher/
│
├── app.py
├── requirements.txt
├── README.md
└── utils/
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run Application

```bash
streamlit run app.py
```

---

## 📊 Matching Logic

The similarity score is calculated using:

```
Similarity = Cosine( TF-IDF(Resume), TF-IDF(Job Description) )
```

The output is displayed as a percentage match.

---

## ✨ Features

✅ Resume PDF Upload  
✅ Automatic Text Extraction  
✅ NLP-Based Matching  
✅ Real-Time Match Score  
✅ Clean & Interactive UI  
✅ Deployable on Streamlit Cloud  

---

## 🚀 Deployment

This application is deployed using **Streamlit Cloud**.

🔗 Live App:  
h

---

## 🔮 Future Enhancements

- 🔍 Skill Gap Analysis  
- 📊 Keyword Highlighting  
- 🤖 Transformer / BERT-based Matching  
- 📄 Multiple Resume Comparison  
- 📈 ATS Score Simulation  

---
## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub!
