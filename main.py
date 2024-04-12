import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("dataset.csv")
df.columns = df.columns.str.replace(' fatalities', '')

df_numeric = df.drop(['Year'], axis=1).select_dtypes(include=[np.number])

# For each column, calculate the IQR
Q1 = df_numeric.quantile(0.25)
Q3 = df_numeric.quantile(0.75)
IQR = Q3 - Q1

# Define a condition for outliers
condition = (df_numeric >= (Q1 - 1.5 * IQR)) | (df_numeric <= (Q3 + 1.5 * IQR))

# Find potential outliers
potential_outliers = df_numeric[condition]

# Print the potential outliers
# print(potential_outliers)

correlation_matrix = df_numeric.corr().T
# print(correlation_matrix)
plt.figure(figsize=(14, 10))
sns.heatmap(correlation_matrix, 
            annot=True, 
            fmt=".2f", 
            cmap='seismic', 
            cbar=True, 
            square=True)
plt.title('Heatmap of Correlation Matrix')
print(correlation_matrix)