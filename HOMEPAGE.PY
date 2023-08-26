import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



data_csv = r'D:\USER\Documents\Homepage-Experiment-Data\homepage_actions.csv'

df = pd.read_csv(data_csv)


print(df.tail())


""" 
1. Match the following characteristics of this dataset:
total number of actions
number of unique users
sizes of the control and experiment groups (i.e., the number of unique users in each group)
"""

# Numbers for control and experiment groups
# Inicial counter
users_A = 0
users_B = 0

# Calculate the number of each one group, control and experiment groups

group_sizes = df.groupby('group')['id'].nunique()

# group sizes in determited stuff
control_group_size = group_sizes['control']
experiment_group_size = group_sizes['experiment']
# Getting the number of unique users and total actions
total_actions = len(df['action'].unique())
unique_users = len(df['id'].unique())

# Timestamp
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Encuentra la primera y la última marca de tiempo en el conjunto de datos
primer_timestamp = df['timestamp'].min()
ultimo_timestamp = df['timestamp'].max()

# Calcula la duración del experimento
duracion_experimento = ultimo_timestamp - primer_timestamp

print("La duración del experimento fue de:", duracion_experimento)


# CTR

unique_clickers = df[df['action'] == 'click']['id'].nunique()
unique_viewers =  df[df['action'] == 'view']['id'].nunique()

# Calculate the ratio
ratio = unique_clickers / unique_viewers if unique_viewers > 0 else 0

print("Number of Unique Clickers:", unique_clickers)
print("Number of Unique Viewers:", unique_viewers)
print("Ratio of Clickers to Viewers:", ratio)
