# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 300
}

total_investment = 0

# User input
stock_name = input("Enter stock name (AAPL, TSLA, GOOG, MSFT): ").upper()
quantity = int(input("Enter quantity: "))

# Calculate investment
if stock_name in stock_prices:
    total_investment = stock_prices[stock_name] * quantity
    print("Total Investment Value =", total_investment)

    # Save result in a text file
    with open("portfolio.txt", "w") as file:
        file.write(f"Stock: {stock_name}\n")
        file.write(f"Quantity: {quantity}\n")
        file.write(f"Total Investment: {total_investment}\n")

    print("Result saved in portfolio.txt")
else:
    print("Stock not found!")
