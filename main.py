# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Simulate a dataset
np.random.seed(42)
data = {
    'overs': np.random.randint(1, 21, 100),  # Random overs between 1 and 20
    'wickets': np.random.randint(0, 11, 100),  # Random wickets between 0 and 10
    'runs': np.random.randint(0, 200, 100),  # Random runs between 0 and 200
}
df = pd.DataFrame(data)
df['total_runs'] = df['runs'] + np.random.randint(0, 100, 100)  # Simulate total runs

# Calculate run rate for feature engineering
df['run_rate'] = df['runs'] / df['overs']

# Generate Box Plot
plt.figure(figsize=(8, 6))
sns.boxplot(data=df[['overs', 'wickets', 'run_rate']])
plt.title('Box Plot for Overs, Wickets, and Run Rate')
plt.show()

# Generate Histogram
plt.figure(figsize=(8, 6))
sns.histplot(df['total_runs'], kde=True, bins=15, color='skyblue')
plt.title('Histogram of Total Runs')
plt.xlabel('Total Runs')
plt.ylabel('Frequency')
plt.show()

# Generate Scatter Plot
plt.figure(figsize=(8, 6))
sns.scatterplot(x=df['overs'], y=df['total_runs'], hue=df['wickets'], palette='viridis', size=df['run_rate'], sizes=(20, 200))
plt.title('Scatter Plot: Overs vs Total Runs')
plt.xlabel('Overs')
plt.ylabel('Total Runs')
plt.show()
