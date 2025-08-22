#  Student Performance Analysis

[![Streamlit App](https://img.shields.io/badge/Streamlit-Live%20App-brightgreen?logo=streamlit)](https://studentperformanceanalysis-wovkzsbhskvyyps34cxbnj.streamlit.app/)

---

This project analyzes student performance data to gain insights into the factors that influence academic outcomes.  
It applies **data preprocessing, exploratory data analysis (EDA), and machine learning models** to predict and understand student success.

---

##  Project Structure

Student_Performance_Analysis/

- `data/` 📊 — Dataset(s) used in the project  
- `notebooks/` 📒 — Jupyter notebooks for EDA & experiments  
- `src/` ⚙️ — Source code for data processing & modeling  
- `app.py` 🌐 — Flask web app (for deployment)  
- `requirements.txt` 📦 — List of dependencies  
- `README.md` 📝 — Project documentation  
---

##  Features

-  Exploratory Data Analysis (EDA) on student dataset  
-  Data preprocessing: handling missing values, encoding, scaling  
-  Machine learning models to predict student performance  
-  Model evaluation with accuracy, precision, recall, and F1-score  
-  Flask integration for web-based prediction (if applicable)

---

##  Dataset

The dataset contains information about students' academic performance and related attributes such as:
- Study time  
- Attendance  
- Parental education  
- Test scores  
- Extra-curricular activities  

---

##  Installation & Setup

### 1. Clone this repository:
   ```bash
   git clone https://github.com/Sonalikasingh17/Student_Performance_Analysis.git
   cd Student_Performance_Analysis
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Train Models
```bash
python src/components/data_ingestion.py
```

### 5. Launch Web App
```bash
streamlit run streamlit_app.py
```

--- 
Made with ❤️ using Python and Streamlit

