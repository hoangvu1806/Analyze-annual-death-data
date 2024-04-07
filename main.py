import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "dataset.csv"
df = pd.read_csv(file_path)

print(df.describe())