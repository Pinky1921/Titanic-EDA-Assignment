# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 13:24:02 2025

@author: Pinky
"""

# Titanic Dataset - Exploratory Data Analysis (EDA)

## 📌 Assignment Title
**Analyzing Titanic Dataset**

## 🎯 Objective
The purpose of this project is to perform Exploratory Data Analysis (EDA) on the Titanic dataset to identify patterns and insights related to the survival of passengers.

---

## 📁 Dataset
- **File Name**: `dataset3 - Sheet1.csv`
- The dataset contains details such as passenger age, gender, ticket class, fare, and survival status.

---

## 🔧 Tasks Completed

### 1. Data Loading
- Loaded the dataset using the pandas library.

### 2. Data Cleaning
- Checked for missing values.
- Filled missing values in the `Age` column using the median age.
- Dropped rows with missing values in the `Embarked` column.
- Removed the `Cabin` column due to too many missing entries.

### 3. Grouping and Aggregation
- Calculated survival rates by gender.
- Calculated survival rates by passenger class.
- Calculated survival rates by both gender and class.

### 4. Visualizations
- **Age Distribution**: Histogram to show the distribution of passenger ages.
- **Survival by Class and Gender**: Barplot showing survival rate based on class and gender.
- **Correlation Heatmap**: Heatmap showing relationships between numeric variables.

---

## 📊 Key Insights

- Most passengers were between 20 and 40 years old.
- Females had a significantly higher chance of survival compared to males.
- 1st class passengers had the highest survival rate, followed by 2nd class and then 3rd class.
- A positive correlation was observed between fare and survival.
- Being female and being in a higher class positively influenced the survival probability.

---
