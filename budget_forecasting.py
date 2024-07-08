# -*- coding: utf-8 -*-
"""Budget forecasting

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bv2RtJxCluiXKWv-QkFrKaz_6r6iidO9
"""

import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA

# Load budget data
file_path = '/content/EB TASSEI-SHA BUDGET.xlsx'
budget_data = pd.read_excel(file_path)

# Perform financial analysis
def financial_analysis(budget_data):
    # Perform basic financial analysis
    analysis_results = {
        'Total Revenue': budget_data['Revenue'].sum(),
        'Total Expenses': budget_data['Expenses'].sum(),
        'Profit': budget_data['Revenue'].sum() - budget_data['Expenses'].sum()
    }
    return analysis_results

# Perform forecasting using ARIMA model
def forecast(budget_data):
    # Extract time series data for forecasting
    time_series_data = budget_data.set_index('Date')['Revenue']

    # Fit ARIMA model
    model = ARIMA(time_series_data, order=(5,1,0))
    fitted_model = model.fit()

    # Forecast future revenue
    forecast_steps = 12
    forecast_values = fitted_model.forecast(steps=forecast_steps)

    return forecast_values

# Provide financial advice based on analysis
def financial_advice(analysis_results, forecast_values):
    # Example financial advice based on analysis and forecast
    if analysis_results['Profit'] > 0:
        advice = "Your business is profitable. Consider reinvesting profits into growth opportunities."
    else:
        advice = "Your business is experiencing losses. Review expenses and revenue streams for potential improvements."

    return advice

def main():
    # Load budget data
    file_path = 'budget.xlsx'
    budget_data = load_budget_data(/content/EB TASSEI-SHA BUDGET.xlsx)

    # Perform financial analysis
    analysis_results = financial_analysis(budget_data)
    print("Financial Analysis:")
    print(analysis_results)

    # Perform forecasting
    forecast_values = forecast(budget_data)
    print("Forecasted Revenue:")
    print(forecast_values)

    # Provide financial advice
    advice = financial_advice(analysis_results, forecast_values)
    print("Financial Advice:")
    print(advice)

if __name__ == "__main__":
    main()