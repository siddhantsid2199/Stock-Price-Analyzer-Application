# Stock Price Analyzer

A Streamlit web application to analyze historical stock price data.

## Description

This application allows users to visualize historical stock data, including closing prices and trading volume. Users can input a stock ticker symbol and select a date range to analyze. The application fetches data from Yahoo Finance using the `yfinance` library and displays interactive charts.

## Features

*   **Stock Ticker Input:** Enter any valid stock ticker symbol (e.g., "AAPL", "GOOG", "MSFT").
*   **Date Range Selection:** Choose a start and end date for the historical data analysis.
*   **Data Visualization:**
    *   Displays a table with the historical stock data (Open, High, Low, Close, Volume).
    *   Shows a line chart for the stock's closing price over time.
    *   Shows a line chart for the stock's trading volume over time.
*   **Dynamic Company Name Display:** Automatically fetches and displays the full company name for the given ticker symbol.
*   **Error Handling:** Provides user-friendly messages for invalid ticker symbols.

## How to Use

1.  **Prerequisites:** Make sure you have Python and `pip` installed.
2.  **Install Dependencies:** Install the required Python libraries using the following command:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the Application:** Start the Streamlit application with the following command:
    ```bash
    streamlit run Stock_Price_Analyzer.py
    ```
4.  **Use the App:**
    *   Open your web browser and navigate to the local URL provided by Streamlit (usually `http://localhost:8501`).
    *   Enter a stock ticker symbol in the text box.
    *   Select a start and end date using the date pickers.
    *   The application will automatically update the charts and data table.

## Dependencies

The application's dependencies are listed in the `requirements.txt` file.
