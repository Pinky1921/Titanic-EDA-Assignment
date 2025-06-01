# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 13:05:58 2025

@author: Pinky
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("dataset3 - Sheet1.csv")
print("Dataset Loaded Successfully\n")
print(df.head())

# -------------------------------
# Data Cleaning
# -------------------------------
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# Fill missing Age with median
df['Age'].fillna(df['Age'].median(), inplace=True)

# Drop rows with missing Embarked
df.dropna(subset=['Embarked'], inplace=True)

# Drop Cabin column due to too many missing values
if 'Cabin' in df.columns:
    df.drop(columns=['Cabin'], inplace=True)

print("\nMissing values after cleaning:")
print(df.isnull().sum())

# -------------------------------
# Grouping and Aggregation
# -------------------------------
print("\nSurvival Rate by Gender:")
print(df.groupby('Sex')['Survived'].mean())

print("\nSurvival Rate by Passenger Class:")
print(df.groupby('Pclass')['Survived'].mean())

print("\nSurvival Rate by Class and Gender:")
print(df.groupby(['Pclass', 'Sex'])['Survived'].mean())

# -------------------------------
# Visualizations
# -------------------------------
sns.set(style="whitegrid")

# Age Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df['Age'], bins=30, kde=True)
plt.title('Age Distribution of Titanic Passengers')
plt.xlabel('Age')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('age_distribution.png')
plt.show()

# Survival by Class and Gender
plt.figure(figsize=(8, 5))
sns.barplot(x='Pclass', y='Survived', hue='Sex', data=df)
plt.title('Survival Rate by Class and Gender')
plt.xlabel('Passenger Class')
plt.ylabel('Survival Rate')
plt.tight_layout()
plt.savefig('survival_by_class_gender.png')
plt.show()

# Correlation Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.savefig('correlation_heatmap.png')
plt.show()

# -------------------------------
# Summary Insights
# -------------------------------
print("\nSummary Insights:")
print("- Most passengers were aged between 20 and 40.")
print("- Females had significantly higher survival rates than males.")
print("- 1st class passengers had the highest survival rate; 3rd class the lowest.")
print("- Fare and being female had positive correlation with survival.")
