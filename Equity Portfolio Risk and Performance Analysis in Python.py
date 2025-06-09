# !pip install yfinance --upgrade --no-cache-dir

# Importing libraries
import numpy as np
import pandas as pd
import plotly.express as px
import yfinance as yf
import datetime as dt

# Setting the timeline
years= 5
end_date= dt.datetime.today()
start_date= end_date - dt.timedelta(years * 365)

# Downloading stock data
tickers= ["JPM", "GS", "BAC", "MS"]

close_df= pd.DataFrame()

for ticker in tickers:
    data= yf.download(ticker, start= start_date, end= end_date)
    close_df[ticker]= data["Close"]

close_df= close_df.dropna()
# print(close_df.head())

# Visualising individual stock values over time
fig1= px.line(close_df, title= "Closing Price Data for Individual Stocks")
fig1.show()

# Calculating log returns
log_returns= np.log(close_df/close_df.shift(1))
log_returns= log_returns.dropna()
# print(log_returns.head())

# Creating an equally weighted portfolio
weights= np.array([1/len(tickers)]*len(tickers))
portfolio_returns= log_returns.dot(weights)
# print(portfolio_returns.head())

# Calculating annualised returns of the portfolio
annualised_portfolio_returns= portfolio_returns.mean()*252
print(f"Annualised portfolio returns= {round((annualised_portfolio_returns * 100), 2)}%")

# Calculating annualised volatility of the portfolio
daily_portfolio_volatility= np.std(portfolio_returns)
annualised_portfolio_volatility= daily_portfolio_volatility * np.sqrt(252)
print(f"Annualised portfolio volatility= {round((annualised_portfolio_volatility * 100), 2)}%")

# Calculating market returns
mkt_data= pd.DataFrame()
mkt_data= yf.download("SPY", start= start_date, end= end_date)["Close"]

mkt_returns= np.log(mkt_data/mkt_data.shift(1))
mkt_returns= mkt_returns.dropna()
print(mkt_returns.head())
print(type(mkt_returns))

# Visualising portfolio value vs market value
portfolio_value= []
portfolio_value.append(1000000)

for i in portfolio_returns:
    portfolio_value.append(portfolio_value[-1]*np.exp(i))

market_value= []
market_value.append(1000000)

for i in mkt_returns["SPY"]:
    market_value.append(market_value[-1]*np.exp(i))

data1= [portfolio_value, market_value]

data1 = pd.DataFrame({
    "Date": mkt_returns.index.insert(0, mkt_returns.index[0]),
    "Market value": market_value,
    "Portfolio value": portfolio_value
})

print(data1)

fig2= px.line(data1, x= "Date",  y=["Market value", "Portfolio value"], title= "Portfolio Value vs Market Value")
fig2.show()

# Calculating annualised market returns
annualised_market_returns= mkt_returns["SPY"].mean()*252
print(f"Annualised market returns= {round((annualised_market_returns * 100), 2)}%")

# Calculating annualised market volatility
daily_mkt_volatility= np.std(mkt_returns["SPY"], axis=0)
annualised_market_volatility= daily_mkt_volatility * np.sqrt(252)
print(f"Annualised market volatility= {round((annualised_market_volatility * 100), 2)}%")

# Calculating beta of the portfolio
# print(np.cov(portfolio_returns, mkt_returns["SPY"]))
beta= (np.cov(portfolio_returns, mkt_returns["SPY"])[1][0])/(np.cov(portfolio_returns, mkt_returns["SPY"])[1][1])
print(f"Beta of the portfolio= {round(beta,2)}")

# Calculating alpha of the portfolio
Rf= 0.05

capm_returns= annualised_market_returns + beta * (annualised_market_returns - Rf)
print(f"CAPM portfolio returns= {round((capm_returns * 100), 2)}%")

alpha= annualised_portfolio_returns - capm_returns
print(f"Alpha of the portfolio= {round((alpha * 100), 2)}%")

# Calculating Sharpe ratio
sharpe_ratio= (annualised_portfolio_returns - Rf)/annualised_portfolio_volatility
print(f"Sharpe ratio of the portfolio= {round(sharpe_ratio,2)}")

# Calculating Treynor ratio
treynor_ratio= (annualised_portfolio_returns - Rf)/beta
print(f"Treynor ratio of the portfolio= {round(treynor_ratio,2)}")

# Calculating Sortino ratio

downside_returns= []
for i in portfolio_returns:
    if i<0:
        downside_returns.append(i)

downside_returns= np.array(downside_returns)
downside_dev= np.std(downside_returns)
print(f"Portfolio's downside volatility= {round((downside_dev * 100), 2)}%")

sortino_ratio= (annualised_portfolio_returns - Rf)/downside_dev
print(f"Sortino ratio of the portfolio= {round(sortino_ratio,2)}")

# Calculating Calmer ratio
max_portfolio_value_position= portfolio_value.index(np.max(portfolio_value))

min_portfolio_value_post_max= portfolio_value[max_portfolio_value_position]

i= max_portfolio_value_position
while i < len(portfolio_value):
    if portfolio_value[i] < min_portfolio_value_post_max:
        min_portfolio_value_post_max = portfolio_value[i]
    i+=1

# print(np.max(portfolio_value))
# print(min_portfolio_value_post_max)

max_drawdown= (np.max(portfolio_value) - min_portfolio_value_post_max)/np.max(portfolio_value)
print(f"Portfolio's maximum drawdown= {round((max_drawdown * 100), 2)}%")

calmer_ratio= annualised_portfolio_returns / max_drawdown
print(f"Calmer ratio of the portfolio= {round(calmer_ratio,2)}")



