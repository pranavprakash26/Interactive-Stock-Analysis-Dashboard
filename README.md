# Interactive-Stock-Analysis-Dashboard
Overview
The Interactive Stock Analysis Dashboard is a dynamic and user-friendly web application built using Bokeh. This application allows users to visualize and compare stock data from Yahoo Finance, apply technical indicators, and analyze trends over customizable time periods.

Features
Stock Comparison: Compare the performance of two different stocks side by side.
Technical Indicators: Apply various technical indicators including:
100 Day Simple Moving Average (SMA)
30 Day Simple Moving Average (SMA)
Linear Regression Line
Custom Date Range: Select custom start and end dates for data analysis.
Interactive Visualization: Utilize interactive plots with zoom, pan, and save tools.
Installation
To get started, clone the repository and install the necessary dependencies:

bash
Copy code
git clone https://github.com/yourusername/stock-analysis-dashboard.git
cd stock-analysis-dashboard
pip install -r requirements.txt
Usage
To run the application, use the following command:

bash
Copy code
bokeh serve --show main.py
Once the server is running, open your web browser and navigate to the provided local URL.

How It Works
Input Fields:

Stock 1 and Stock 2: Enter the ticker symbols for the two stocks you want to analyze.
Start Date and End Date: Choose the date range for the data.
Indicators: Select the technical indicators to apply.
Data Loading:

The application fetches historical stock data from Yahoo Finance based on the provided ticker symbols and date range.
Data Processing:

The selected technical indicators are calculated and added to the data.
Visualization:

The processed data is plotted, showing candlestick charts along with the selected indicators.
Example

Dependencies
Python 3.7+
Bokeh
yfinance
numpy
