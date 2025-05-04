import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate a sample dataset
data = {
    'Date': pd.date_range(start='2023-01-01', periods=10, freq='D'),
    'Revenue': np.random.randint(1000, 5000, size=10),
    'Expenses': np.random.randint(500, 2000, size=10)
}
df = pd.DataFrame(data)

# Calculate profit
df['Profit'] = df['Revenue'] - df['Expenses']

# Save to CSV
df.to_csv('financial_data.csv', index=False)

# Plot revenue and profit trends
plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['Revenue'], label='Revenue', marker='o')
plt.plot(df['Date'], df['Profit'], label='Profit', marker='x')
plt.legend()
plt.title('Revenue & Profit Trends')
plt.xlabel('Date')
plt.ylabel('Amount')
plt.xticks(rotation=45)
plt.grid()
plt.show()

