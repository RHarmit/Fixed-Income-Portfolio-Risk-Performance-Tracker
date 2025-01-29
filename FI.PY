import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

# Fetch historical bond yield data (Example: US 10-Year Treasury Bond)
bond_ticker = "^TNX"  # US 10-Year Treasury Yield
data = yf.download(bond_ticker, start="2023-01-01", end="2024-01-01")

data['Daily Return'] = data['Adj Close'].pct_change()
data.dropna(inplace=True)

# Calculate Key Fixed Income Metrics
def calculate_metrics(data):
    avg_yield = data['Adj Close'].mean()
    yield_volatility = data['Daily Return'].std()
    var_95 = np.percentile(data['Daily Return'], 5)  # 5% VaR estimation
    
    return avg_yield, yield_volatility, var_95

avg_yield, yield_volatility, var_95 = calculate_metrics(data)

# Visualizing Bond Yield Movements
plt.figure(figsize=(10, 5))
plt.plot(data.index, data['Adj Close'], label='US 10Y Treasury Yield', color='blue')
plt.xlabel("Date")
plt.ylabel("Yield (%)")
plt.title("US 10-Year Treasury Yield Trends")
plt.legend()
plt.grid()
plt.show()

# Output the results
print(f"Average Yield: {avg_yield:.2f}%")
print(f"Yield Volatility: {yield_volatility:.4f}")
print(f"Value at Risk (95% Confidence): {var_95:.4f}")
