import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# 1. Load the datasets
# =========================
trader_df = pd.read_csv("trader_data.csv")
sentiment_df = pd.read_csv("fear_greed.csv")

print("Trader Data Columns:")
print(trader_df.columns)

print("\nSentiment Data Columns:")
print(sentiment_df.columns)

# =========================
# 2. Convert timestamps to DATE
# =========================
# Trader dataset:
# Timestamp is in MILLISECONDS
trader_df['date'] = pd.to_datetime(
    trader_df['Timestamp'],
    unit='ms',
    errors='coerce'
).dt.date

# Sentiment dataset:
# timestamp is in SECONDS
sentiment_df['date'] = pd.to_datetime(
    sentiment_df['timestamp'],
    unit='s',
    errors='coerce'
).dt.date

# =========================
# 3. Merge both datasets on date
# =========================
merged_df = pd.merge(
    trader_df,
    sentiment_df[['date', 'classification']],
    on='date',
    how='inner'
)

print("\nMerged Data Preview:")
print(merged_df.head())

# =========================
# 4. Trader Performance Analysis
# =========================
# Using Closed PnL as performance metric
performance = merged_df.groupby('classification')['Closed PnL'].mean()

print("\nAverage Trader PnL by Market Sentiment:")
print(performance)

# =========================
# 5. Visualization
# =========================
plt.figure(figsize=(8, 5))
sns.barplot(x=performance.index, y=performance.values)
plt.title("Trader Performance vs Bitcoin Market Sentiment")
plt.xlabel("Market Sentiment")
plt.ylabel("Average Closed PnL")
plt.tight_layout()
plt.show()
