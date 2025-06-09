# 📊 Equity Portfolio Risk and Performance Analysis in Python

This repository contains a Python script for analyzing the risk and performance metrics of an equity portfolio using historical market data.

---

## 🚀 Features

- Download historical equity price data using **Yahoo Finance**
- Compute:
  - Log returns
  - Annualized return and volatility
  - Portfolio beta and alpha
  - Maximum drawdown
  - Sharpe, Treynor, Sortino, and Calmar ratios
- Visualize:
  - Individual stock closing prices
  - Portfolio vs market value growth over time

---

## 📁 Files

- `investment_analysis.py`: Main script performing the analysis.
- `requirements.txt` *(optional)*: Contains required packages (if you decide to add one).

---

## 🧮 Libraries Used

- `numpy`
- `pandas`
- `plotly`
- `yfinance`
- `datetime`

---

## 📌 Portfolio Details

- Equal-weighted portfolio of four U.S. financial stocks: `JPM`, `GS`, `BAC`, `MS`
- Benchmark: `SPY` (S&P 500 ETF)
- Investment horizon: Last 5 years

---

## 📈 Risk & Performance Metrics Calculated

| Metric                 | Description                                            |
|------------------------|--------------------------------------------------------|
| **Annualized Return**  | Average yearly return of the portfolio                 |
| **Volatility**         | Standard deviation of returns, annualized              |
| **Beta**               | Sensitivity of portfolio to market movements           |
| **Alpha**              | Excess return over CAPM-predicted return               |
| **Max Drawdown**       | Worst peak-to-trough decline                           |
| **Sharpe Ratio**       | Risk-adjusted return using total volatility            |
| **Treynor Ratio**      | Risk-adjusted return using beta                        |
| **Sortino Ratio**      | Risk-adjusted return penalizing only downside          |
| **Calmar Ratio**       | Return to maximum drawdown                             |

---

## 📊 Sample Visuals

- Line chart of closing prices for individual stocks
- Line chart comparing portfolio value vs. market value over time

---
