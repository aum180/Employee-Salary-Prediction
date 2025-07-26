# Employee Salary Prediction Project

## Overview
This project provides a comprehensive solution for predicting employee salaries based on various professional attributes. It includes a complete machine learning pipeline for salary prediction and an interactive Streamlit web application for visualizing results and making predictions.

## Key Components
  1. Data Analysis & Preprocessing: Comprehensive data cleaning, feature engineering, and outlier handling
  
  2. Machine Learning Modeling: Implementation and tuning of multiple regression algorithms
  
  3. Model Evaluation: Rigorous performance assessment using R², RMSE, and MAE metrics
  
  4. Streamlit Web App: Interactive dashboard for salary prediction and visualization

## Features
### 🧠 Machine Learning Pipeline
  - Advanced feature engineering with experience ratios and seniority flags
  - Outlier handling using winsorization
  - One-hot encoding for categorical features
  - Standard scaling for numerical features
  - Hyperparameter tuning with GridSearchCV
  - Evaluation of multiple algorithms:
    - Random Forest Regressor
    - XGBoost
    - Gradient Boosting
    - ElasticNet
    - Ridge Regression

### 📊 Streamlit Application
- Interactive Prediction: Input employee attributes to get salary predictions
- Visual Analytics:
  - Salary distribution by education level
  - Department/location salary comparisons
  - Experience-performance relationships
- Industry Benchmarking: Compare predictions against industry standards
- Professional Insights: Education premium and performance impact analysis
- Responsive Design: Mobile-friendly interface with premium styling

## Results
The Random Forest model achieved the best performance:
  - Test R²: 0.7028
  - RMSE: 42,355.24
  - MAE: 28,169.77

## Getting Started
### Prerequisites
  - Python 3.7+
  - Required packages: pandas, numpy, scikit-learn, xgboost, streamlit, plotly

### Installation
1. Clone the repository:
```
git clone https://github.com/your-username/employee-salary-prediction.git
cd employee-salary-prediction
```

2. Install dependencies:
```
pip install -r requirements.txt
```
### Usage
1. Run the Jupyter notebook to train models:
```
jupyter notebook Employee_Salary_Prediction.ipynb
```

2. Launch the Streamlit app:
```
streamlit run app.py
```

## Project Structure
```
├── data/                    # Dataset directory
│   └── Employee_Salary_Dataset.csv
├── notebooks/
│   └── Employee_Salary_Prediction.ipynb   # Jupyter notebook
├── app.py                   # Streamlit application
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

## Key Findings
1. Higher education levels (Master's/PhD) command significant salary premiums
2. Engineering and Finance departments offer the highest compensation
3. Top performers (rating 5) earn up to 40% more than average performers
4. Urban locations have 20% higher salaries compared to rural areas
5. The 10-15 year experience range shows the highest salary growth

## Contributing
Contributions are welcome! Please fork the repository and submit pull requests.
