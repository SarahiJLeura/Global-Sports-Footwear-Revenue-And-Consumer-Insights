# Predicting Product Demand in the Global Sports Footwear Market (2018-2026)

## Project Overview

This project analyzes and predicts **product demand (units sold)** in the global sports footwear market using machine learning techniques.

It applies the **Knowledge Discovery in Databases (KDD) process** to perform:
- Data preprocessing
- Feature selection
- Dimensionality reduction (PCA)
- Predictive modeling (regression)
- Model evaluation and comparison

The main objective is to understand which factors influence footwear sales and evaluate the performance of different machine learning models.

---

## Problem Statement

The goal is to predict the number of **units sold per transaction** using supervised regression models.

This project answers:
- What factors influence footwear demand?
- Can we predict sales using customer and product data?
- Which machine learning models perform best?

---

## Dataset Information

> **Important Note:**  
> The dataset appears to be **synthetic**, as identified during analysis due to highly uniform distributions and weak relationships between variables.

### 📌 Source Dataset
Kaggle – Sports Footwear Sales & Consumer Behavior  
https://www.kaggle.com/datasets/aliiihussain/sports-footwear-sales-and-consumer-behavior/

### Dataset Summary
- 30,000 records
- 18 attributes
- Time period: 2018–2026
- Global retail + online sales data

### Features
- **Product:** brand, category, model_name, size, color
- **Pricing:** base_price_usd, discount_percent, final_price_usd
- **Customer:** income_level, rating, gender, country
- **Sales:** sales_channel, payment_method
- **Target variable:** units_sold

---

## Methodology (KDD Process)

The project follows the full **KDD pipeline**:

1. **Data Selection**
2. **Data Cleaning**
   - Missing values check (none found)
   - Outlier analysis (validated, not removed)
3. **Data Transformation**
   - Feature engineering (year, month, dayofweek)
4. **Feature Selection**
   - Pearson Correlation (numerical features)
   - Mutual Information (categorical + numerical)
5. **Dimensionality Reduction**
   - PCA (no meaningful separation found)
6. **Data Mining (Models)**
   - Decision Tree Regressor
   - Random Forest Regressor
   - Gradient Boosting Regressor
7. **Evaluation Metrics**
   - MAE
   - MSE
   - R² Score

---

## Key Findings

- Features show **very weak correlation** with target variable.
- Mutual Information scores are extremely low.
- PCA shows **no separable structure** in data.
- All models produced **negative R² values**, meaning:
  - Models performed worse than a simple baseline predictor.

### Conclusion
The dataset is likely **synthetic or artificially generated**, limiting its predictive power.

---

## Machine Learning Models

The following models were trained and optimized:

- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor

Hyperparameter tuning:
- GridSearchCV
- RandomizedSearchCV

---

## References

[1] Farshad Abdulazeez. Understanding decision tree regressor: An in-depth intu-
ition, 2023. URL https://farshadabdulazeez.medium.com/understanding-
decision-tree-regressor-an-in-depth-intuition-a1d3af182efd. Ac-
cessed: May 15, 2026.
26
[2] D. Barbara. Knowledge discovery in databases (kdd), 2026. URL https://www2.
cs.uregina.ca/~dbd/cs831/notes/kdd/1_kdd.html. Accessed: Feb. 18, 2026.
[3] Footwear News. Top footwear brands in the global market, 2025.
URL https://wwd.com/footwear-news/shoe-industry-news/nike-adidas-
skechers-new-balance-top-footwear-brands-1238684372/. Accessed: May
15, 2026.
[4] GeeksforGeeks. Skewness of statistical data. https://www.geeksforgeeks.org/
data-science/program-find-skewness-statistical-data/, Jul 2024. Last
updated Jul. 24, 2024.
[5] Grand View Research. Athletic footwear market size & share analysis re-
port, 2024–2030, 2024. URL https://www.grandviewresearch.com/industry-
analysis/athletic-footwear-market. Accessed: Feb. 18, 2026.
[6] A. Hussain. Sports footwear sales & consumer behavior, 2026. [Online]. Avail-
able: https://www.kaggle.com/datasets/aliiihussain/sports-footwear-
sales-and-consumer-behavior/. Accessed: Feb. 18, 2026.
[7] IBM. What is gradient boosting?, 2024. URL https://www.ibm.com/think/
topics/gradient-boosting. Accessed: May 15, 2026.
[8] IBM. What is random forest?, 2024. URL https://www.ibm.com/think/topics/
random-forest. Accessed: May 15, 2026.
[9] Analytics Vidhya. Mae, mse, rmse, coefficient of determination, adjusted r squared
— which metric is better?, 2021. URL https://medium.com/analytics-
vidhya/mae-mse-rmse-coefficient-of-determination-adjusted-r-
squared-which-metric-is-better-cd0326a5697e. Accessed: May 15,
2026.

---

## GitHub Pages (Live Demo)

The project report is published using GitHub Pages:

https://sarahijleura.github.io/Global-Sports-Footwear-Revenue-And-Consumer-Insights/

⚠️ If the HTML is not updating, make sure:

The file is named index.html
It is located in the root or /docs folder
GitHub Pages is configured correctly in repository settings

---

## Google Colab Notebook

Run the project online:

https://colab.research.google.com/drive/1g1eIO1kwRSmHdVFq0CkI0VWVZmeMzZSn?usp=sharing

---

## Author

Sarahi Jimenez Leura
Intelligent Systems Engineering
Autonomous University of San Luis Potosi