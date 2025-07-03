import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns

# Load Excel
file_path = "C:\\ML module project\Machine Learning Module Project - Economic status of different regions..xlsx"
df = pd.read_excel(file_path, sheet_name="Neural Network Data")

# Extract numeric part from 'economic_category' like "6 \10"
df['economic_score'] = df['economic_category'].astype(str).str.extract(r'(\d+)').astype(float)

# Drop rows with missing values in score or important features
features = [
    'population',
    'yearly_percentage_change',
    'median_age',
    'fertility_rate',
    'density',
    'happiness_index',
    'interest_rates',
    'taxes'
]
df_clean = df.dropna(subset=['economic_score'] + features)

# Sort and display
df_sorted = df_clean[['country_name', 'economic_score']].sort_values(by='economic_score', ascending=False)
print(df_sorted)

# Visualization
plt.figure(figsize=(14, 6))
sns.barplot(data=df_sorted, x='country_name', y='economic_score', palette='coolwarm')
plt.xticks(rotation=90)
plt.title("Economic Category Score (out of 10) by Country")
plt.ylabel("Economic Score")
plt.xlabel("Country")
plt.tight_layout()
plt.show()
