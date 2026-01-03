# trader-behavior-insights
Analysis of trader performance vs Bitcoin market sentiment using Hyperliquid trading data and Fear &amp; Greed Index.
# Trader Behavior Insights

## Objective
The objective of this project is to analyze the relationship between Bitcoin market sentiment
(Fear/Greed) and trader performance using historical trading data from Hyperliquid.

## Datasets Used
1. Bitcoin Fear & Greed Index
   - Columns: date, classification
2. Hyperliquid Historical Trader Data
   - Includes: account, execution price, size, side, leverage, closed PnL, timestamp

## Methodology
- Converted timestamps from both datasets into daily date format
- Merged trader data with sentiment data using date
- Used Closed PnL as a metric to evaluate trader performance
- Analyzed average profitability across different market sentiment regimes
- Visualized results using bar charts

## Key Insights
- Traders tend to generate higher average profits during Greed periods
- Fear and Extreme Fear periods show increased losses
- Market sentiment significantly influences trader risk-taking behavior
- Sentiment indicators can be used to improve trading risk management

## Tools & Technologies
- Python
- Pandas
- Matplotlib
- Seaborn

## Conclusion
Combining market sentiment with trader behavior provides valuable insights that can support
smarter trading strategies and better risk control.
