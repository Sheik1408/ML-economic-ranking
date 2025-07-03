import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

st.set_page_config(page_title="Economic Ranking", layout="wide")

st.title("🌍 Economic Category Score Analyzer")
st.markdown("Upload an Excel file with country data to generate economic scores out of 10.")

uploaded_file = st.file_uploader("C:\economic ranking\Machine Learning Module Project - Economic status of different regions.xlsx", type=["xlsx"])

if uploaded_file:
    sheet_name = "Neural Network Data"
    try:
        df = pd.read_excel(uploaded_file, sheet_name=sheet_name)

        # Extract numeric economic score
        df['economic_score'] = df['economic_category'].astype(str).str.extract(r'(\d+)').astype(float)

        # Drop NaNs and filter needed columns
        features = [
            'population', 'yearly_percentage_change', 'median_age',
            'fertility_rate', 'density', 'happiness_index',
            'interest_rates', 'taxes'
        ]
        df_clean = df.dropna(subset=['economic_score'] + features)

        # Show table
        st.subheader("📊 Economic Scores by Country")
        result_df = df_clean[['country_name', 'economic_score']].sort_values(by='economic_score', ascending=False)
        st.dataframe(result_df, use_container_width=True)

        # Plot
        st.subheader("📈 Economic Score Visualization")
        fig, ax = plt.subplots(figsize=(14, 6))
        sns.barplot(data=result_df, x='country_name', y='economic_score', palette='viridis', ax=ax)
        plt.xticks(rotation=90)
        plt.ylabel("Economic Score (out of 10)")
        plt.title("Economic Ranking by Country")
        st.pyplot(fig)

    except Exception as e:
        st.error(f"❌ Error reading the file: {e}")
