
---

# CORD-19 Dataset Exploration

## 📌 Project Overview

This project explores the **CORD-19 dataset** (metadata.csv) to analyze COVID-19–related research publications.
The assignment covers the full **data science workflow**:

1. Data loading and exploration
2. Data cleaning and preparation
3. Data analysis and visualization
4. Building an interactive **Streamlit application**
5. Documentation and reflection

---

## 🗂 Dataset

* **Source**: CORD-19 metadata.csv
* **Key columns**:

  * `title` – paper titles
  * `abstract` – research abstracts
  * `publish_time` – publication dates
  * `journal` – publishing journals
  * `authors` – author names
  * `source_x` – data sources

---

## ⚙️ Requirements

Install the required libraries before running the scripts:

```bash
pip install pandas numpy matplotlib seaborn streamlit wordcloud
```

---

## 🚀 How to Run

### 1. Run the Jupyter Notebook / Python Script

For exploration and analysis:

```bash
python analysis.py
```

or open the Jupyter Notebook (if provided).

### 2. Launch the Streamlit App

For interactive visualization:

```bash
streamlit run app.py
```

---

## 📊 Features

### Analysis Performed

* Publications trend by year
* Top 10 journals by number of publications
* Most frequent words in titles (word cloud)
* Distribution of publications by source

### Visualizations

* Bar charts (Matplotlib & Seaborn)
* Word cloud of paper titles
* Interactive filters in Streamlit (year range selector)

---

## 📝 Challenges

* Large dataset size → required working with subsets for faster processing.
* Missing values in key columns (abstracts, authors, publish\_time).
* Data cleaning for dates to enable time-series analysis.

---

## 🎯 Learnings

* Hands-on experience with **data cleaning, exploration, and visualization**.
* Using **Seaborn and Matplotlib** for effective charts.
* Building a simple **Streamlit dashboard**.
* Better understanding of incremental debugging and data wrangling.

---

## 📂 Project Structure

```
│── app.py              # Streamlit app  
│── analysis.py         # Data cleaning & visualization  
│── metadata.csv        # Dataset (not included in repo if too large)  
│── README.md           # Project documentation  
│── report.docx/md      # Short report on findings  
```

---

✍️ **Author**: \Abosede Bamidele
📅 **Date**: \22/09/2025

---
