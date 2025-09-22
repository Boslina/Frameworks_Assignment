
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# load data
df = pd.read_csv("sample-metadata.csv")

# convert publish_time to datetime
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
# extract year
df['year'] =  df['publish_time'].dt.year

st.title("CORD-19 Data Explorer")
st.write("An interactive dashboard for exploring COVID-19 research papers.")

# --- Sidebar filters ---
year_range = st.slider("Select year range", 2015, 2022, (2019, 2021))

# Filter dataset
filtered = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# --- Publications by Year ---
st.subheader("Publications by Year")
year_counts = filtered['year'].value_counts().sort_index()
fig, ax = plt.subplots()
sns.barplot(x=year_counts.index, y=year_counts.values, palette="viridis", ax=ax)
ax.set_xlabel("Year")
ax.set_ylabel("Number of Publications")
st.pyplot(fig)

# --- Top Journals ---
st.subheader("Top 10 Journals")
top_journals = filtered['journal'].value_counts().head(10)
fig, ax = plt.subplots()
sns.barplot(x=top_journals.values, y=top_journals.index, palette="magma", ax=ax)
ax.set_xlabel("Publications")
ax.set_ylabel("Journal")
st.pyplot(fig)

# --- Sample Data ---
st.subheader("Sample Data")
st.dataframe(filtered[['title','journal','year']].head(10))

# Run the app on bash by typing steamlit run app.py in the folder