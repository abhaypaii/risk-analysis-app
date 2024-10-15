
# Portfolio Risk Analysis and Quantitative Optimisation


This is a Streamlit web application that allows users to input their portfolio assets and receive a comprehensive ticker summary, including news, stock prices, and returns. The app calculates quantitative risk metrics such as Value at Risk (VaR), volatility, Sharpe and Sortino ratios, and maximum drawdown. Additionally, it visualizes the efficient frontier and Capital Allocation Line (CAL) with suggested optimal portfolio allocations.
## Project URL

[risk-analysis-app.streamlit.app](risk-analysis-app.streamlit.app)


# Table of Contents

1. Input page
2. Stock Dashboard
3. Risk Analysis
4. Portfolio Optimisation
   
# Input Page

![Input Page](https://github.com/abhaypaii/risk-analysis-app/blob/main/img/Input%20Page.png?raw=true)

This is the landing page where the user will input each stock of their portofolio and the respective value.

I have added a feature where the user can add a new stock or delete any stock as required.

I have also added a button for data validation. If the data is not valid, the button to go to the next page will not be enabled.

# Stock Dashboard

![Dashboard](https://github.com/abhaypaii/risk-analysis-app/blob/main/img/Dashboard.png?raw=true)

After validation, the app goes to the stock dashboard page.

The user can choose what stock they want to analyse and what frequency of returns do they want to look at.

All of this was made using the yfinance library, and plotted using streamlit's plotly integration

# Risk Analysis

![Risk Analysis](https://github.com/abhaypaii/risk-analysis-app/blob/main/img/Risk%20Analysis.png?raw=true)

This next section displays two horizontal stacked bar charts, which represent the portfolio weight and the portfolio risk contribution of each stock respectively.

The page also summarize the total value of the portfolio along with the annualised returns and risk.

The page then has 4 tabs, each displaying one aspect of quantitative metrics of the portfolio, with a description of what it implies about the risk-return tradeoff of the portfolio.


# Optimal Allocation

![Risk Analysis](https://github.com/abhaypaii/risk-analysis-app/blob/main/img/Optimisation.png?raw=true)

The final page displays the best options for the portfolio allocation based on hypothetised random weights assigned to each asset.

Each tab displays the hypotehtical portfolios with the most returns, least risk, and the best overall risk-return tradeoff.

Each tab also has suggestions to the investor and the implication of how the value of each stock shoudl be customized to achieve the said risk and return.
# Authors

- [@abhaypaii](https://www.github.com/abhaypaii)

