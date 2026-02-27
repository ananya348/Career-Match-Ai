import streamlit as st
import pandas as pd
from pypdf import PdfReader
import re
from collections import Counter
import requests

# ======================================
# 🔐 RAPIDAPI KEY
# ======================================
RAPIDAPI_KEY = "5a8ec44632msh3451993135b90ddp1af2dejsn40375ac948f2"

# ======================================
# 🧠 SOFTWARE ENGINEERING DOMAINS
# ======================================
# ======================================
# 🧠 ADVANCED SOFTWARE ENGINEERING DOMAINS
# ======================================

SOFTWARE_ENGINEER_DOMAINS = {

    # 🌐 FRONTEND ENGINEERING
    "Frontend Engineering": [
        # Core
        "html", "html5", "css", "css3", "sass", "less",
        "javascript", "typescript",

        # Frameworks
        "react", "redux", "nextjs", "gatsby",
        "angular", "vue", "nuxt", "svelte",

        # UI Libraries
        "bootstrap", "tailwind", "material ui",
        "chakra ui", "ant design",

        # Tools
        "webpack", "vite", "babel", "eslint",
        "storybook", "figma",

        # Concepts
        "responsive design", "web accessibility",
        "cross browser compatibility",
        "seo optimization", "progressive web apps"
    ],

    # ⚙ BACKEND ENGINEERING
    "Backend Engineering": [
        # Languages
        "python", "java", "c#", "node", "golang", "ruby", "php",

        # Python
        "django", "flask", "fastapi",

        # Java
        "spring", "spring boot", "hibernate",

        # Node
        "express", "nestjs",

        # PHP
        "laravel", "codeigniter",

        # .NET
        "asp.net", "asp.net core",

        # APIs
        "rest api", "graphql", "grpc",
        "microservices", "authentication",
        "jwt", "oauth",

        # Concepts
        "caching", "redis",
        "rate limiting",
        "event driven architecture"
    ],

    # 🔄 FULL STACK ENGINEERING
    "Full Stack Engineering": [
        "react", "angular", "vue",
        "node", "express",
        "django", "flask",
        "spring boot",
        "mongodb", "mysql", "postgresql",
        "redis",
        "rest api", "graphql",
        "docker", "kubernetes",
        "aws", "azure", "gcp",
        "ci/cd", "unit testing"
    ],

    # ☁ CLOUD ENGINEERING
    "Cloud Engineering": [
        # Providers
        "aws", "azure", "gcp",

        # AWS
        "ec2", "s3", "lambda", "rds", "cloudfront",
        "iam", "vpc", "cloudwatch",

        # Azure
        "azure functions", "azure devops",
        "azure app service",

        # GCP
        "google compute engine",
        "cloud run", "bigquery",

        # IaC
        "terraform", "cloud formation",
        "serverless architecture",

        # Concepts
        "cloud security",
        "cloud networking",
        "high availability",
        "load balancing"
    ],

    # 🚀 DEVOPS ENGINEERING
    "DevOps Engineering": [
        "docker", "kubernetes", "helm",
        "jenkins", "github actions",
        "gitlab ci", "circleci",
        "terraform", "ansible",
        "chef", "puppet",
        "linux", "bash",
        "shell scripting",
        "nginx", "apache",
        "prometheus", "grafana",
        "elk stack",
        "ci/cd pipelines",
        "infrastructure as code"
    ],

    # 🤖 ARTIFICIAL INTELLIGENCE
    "Artificial Intelligence": [
        "machine learning",
        "deep learning",
        "artificial intelligence",
        "nlp", "computer vision",
        "speech recognition",

        # Libraries
        "tensorflow", "keras",
        "pytorch",
        "scikit-learn",
        "opencv",

        # Modern AI
        "transformers",
        "huggingface",
        "llms",
        "langchain",

        # Concepts
        "model training",
        "model deployment",
        "reinforcement learning"
    ],

    # 📊 DATA ENGINEERING
    "Data Engineering": [
        "sql", "mysql", "postgresql",
        "mongodb", "cassandra",
        "hadoop", "spark",
        "hive", "pig",
        "kafka", "airflow",
        "etl pipelines",
        "data warehousing",
        "snowflake", "redshift",
        "bigquery",
        "data lakes"
    ],

    # 📱 ANDROID DEVELOPMENT
    "Android Development": [
        "android", "kotlin", "java",
        "android studio",
        "jetpack compose",
        "xml layouts",
        "firebase",
        "retrofit",
        "room database"
    ],

    # 🍎 iOS DEVELOPMENT
    "iOS Development": [
        "ios", "swift", "objective-c",
        "xcode",
        "swiftui",
        "core data",
        "cocoapods",
        "testflight"
    ],

    # 🔐 CYBERSECURITY ENGINEERING
    "Cybersecurity Engineering": [
        "cybersecurity",
        "penetration testing",
        "ethical hacking",
        "network security",
        "application security",
        "cryptography",
        "siem",
        "owasp",
        "burp suite",
        "metasploit",
        "firewalls",
        "incident response"
    ],

    # 🧪 QA / TEST ENGINEERING
    "QA / Test Engineering": [
        "manual testing",
        "test automation",
        "selenium",
        "cypress",
        "playwright",
        "pytest",
        "junit",
        "testng",
        "unit testing",
        "integration testing",
        "performance testing",
        "load testing",
        "jira",
        "bug tracking"
    ],

    # 🗄 DATABASE ENGINEERING
    "Database Engineering": [
        "mysql", "postgresql",
        "oracle", "sqlite",
        "mongodb", "redis",
        "cassandra",
        "elasticsearch",
        "database design",
        "query optimization",
        "indexing",
        "replication",
        "sharding"
    ],

    # 🖥 SYSTEMS PROGRAMMING
    "Systems Programming": [
        "c", "c++", "rust", "go",
        "assembly",
        "memory management",
        "operating systems",
        "multithreading",
        "concurrency",
        "linux kernel",
        "socket programming"
    ],

    # 🎮 GAME DEVELOPMENT
    "Game Development": [
        "unity", "unreal engine",
        "c#", "c++",
        "game physics",
        "3d rendering",
        "opengl", "directx",
        "shader programming",
        "multiplayer networking"
    ],

    # 🔗 BLOCKCHAIN DEVELOPMENT
    "Blockchain Development": [
        "blockchain",
        "solidity",
        "web3",
        "smart contracts",
        "ethereum",
        "hyperledger",
        "defi",
        "nft",
        "cryptography",
        "truffle",
        "hardhat"
    ],

    # 🏗 SOFTWARE ARCHITECTURE
    "Software Architecture": [
        "microservices",
        "system design",
        "design patterns",
        "distributed systems",
        "event driven architecture",
        "monolithic architecture",
        "rest api",
        "graphql",
        "scalability",
        "high availability"
    ]
}

# ======================================
# 📂 LOAD CSV
# ======================================
@st.cache_data
def load_data():
    df = pd.read_csv("all_job_post.csv")
    df.columns = df.columns.str.strip().str.lower()
    return df

df = load_data()

# ======================================
# 📄 Extract PDF Text
# ======================================
def extract_text_from_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + " "
    return text

# ======================================
# 🧠 Extract Skills
# ======================================
def extract_skills(text, skill_list):
    found = []
    text_lower = text.lower()

    for skill in skill_list:
        pattern = r'\b' + re.escape(skill.lower()) + r'\b'
        if re.search(pattern, text_lower):
            found.append(skill)

    return found

# ======================================
# 📊 Extract Experience
# ======================================
def extract_experience(text):
    matches = re.findall(r'(\d+)\+?\s+years?', text.lower())
    if matches:
        return max([int(m) for m in matches])
    return 0

# ======================================
# 🌐 Fetch Jobs
# ======================================
def fetch_jobs(skills, experience, role):

    if not skills:
        return []

    top_skills = [skill for skill, _ in Counter(skills).most_common(3)]
    query = f"{role} {' '.join(top_skills)} {experience} years"

    url = "https://jsearch.p.rapidapi.com/search"

    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }

    params = {
        "query": query,
        "page": "1",
        "num_pages": "1",
        "country": "in"
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        st.error(f"API Error: {e}")
        return []

    jobs = []

    if "data" in data:
        for item in data["data"][:10]:
            jobs.append({
                "title": item.get("job_title"),
                "company": item.get("employer_name"),
                "location": item.get("job_city"),
                "apply_link": item.get("job_apply_link")
            })

    return jobs

# ======================================
# 🚀 STREAMLIT UI
# ======================================
st.set_page_config(page_title="AI Resume Job Matcher", layout="wide")

st.title("🤖 AI Resume Job Matcher")
st.divider()

# ======================================
# 🎯 CATEGORY + SUBCATEGORY
# ======================================
st.subheader("🎯 Select Job Preferences")

col1, col2 = st.columns(2)

csv_categories = sorted(df["category"].dropna().unique())
all_categories = ["Software Engineer"] + csv_categories

with col1:
    selected_category = st.selectbox("📂 Category", all_categories)

with col2:
    if selected_category == "Software Engineer":
        selected_subcategory = st.selectbox(
            "📁 Domain",
            sorted(SOFTWARE_ENGINEER_DOMAINS.keys())
        )
    else:
        filtered_df = df[df["category"] == selected_category]
        job_titles = sorted(filtered_df["job_title"].dropna().unique())

        selected_subcategory = st.selectbox(
            "📁 Job Title",
            job_titles
        )

st.divider()

# ======================================
# 📄 Resume Upload
# ======================================
uploaded_file = st.file_uploader("📄 Upload Resume (PDF only)", type=["pdf"])

if uploaded_file is not None:

    with st.spinner("Analyzing Resume..."):
        resume_text = extract_text_from_pdf(uploaded_file)

        if selected_category == "Software Engineer":
            master_skills = SOFTWARE_ENGINEER_DOMAINS[selected_subcategory]
        else:
            job_filtered_df = df[df["job_title"] == selected_subcategory]
            all_skills = []

            for skills in job_filtered_df["job_skill_set"].dropna():
                all_skills.extend([s.strip() for s in skills.split(",")])

            master_skills = list(set(all_skills))

        extracted_skills = extract_skills(resume_text, master_skills)
        experience = extract_experience(resume_text)

    st.success("Resume Analysis Complete!")

    colA, colB = st.columns(2)

    with colA:
        st.subheader("🧠 Extracted Skills")

        if extracted_skills:
            skill_html = '<div style="display:flex;flex-wrap:wrap;gap:8px;">'
            for skill in sorted(set(extracted_skills)):
                skill_html += (
                    '<span style="background:#1f77b4;color:white;'
                    'padding:6px 12px;border-radius:20px;'
                    'font-size:14px;display:inline-block;">'
                    + skill +
                    '</span>'
                )
            skill_html += '</div>'
            st.markdown(skill_html, unsafe_allow_html=True)
        else:
            st.warning("No skills detected.")

    with colB:
        st.subheader("📊 Experience")
        st.metric("Years", experience)

    st.divider()

    if st.button("🚀 Find Jobs"):

        with st.spinner("🔎 Searching for jobs... Please wait"):
            jobs = fetch_jobs(extracted_skills, experience, selected_subcategory)

        if jobs:
            st.success(f"✅ Found {len(jobs)} jobs")

            for job in jobs:
                st.markdown(f"### {job['title']}")
                st.write(f"🏢 {job['company']}")
                st.write(f"📍 {job['location']}")
                st.markdown(
                    f'<a href="{job["apply_link"]}" target="_blank">'
                    f'<button style="background:#28a745;color:white;'
                    f'border:none;padding:8px 16px;border-radius:6px;">'
                    f'Apply Now</button></a>',
                    unsafe_allow_html=True
                )
                st.divider()
        else:
            st.warning("No jobs found.")