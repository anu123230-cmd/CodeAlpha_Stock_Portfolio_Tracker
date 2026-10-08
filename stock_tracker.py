# Stock Portfolio Tracker
# CodeAlpha Python Programming Internship

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 400,
    "AMZN": 180
}

total_investment = 0

print("================================")
print("     STOCK PORTFOLIO TRACKER")
print("================================")

while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available.")
        print("Available stocks:", ", ".join(stock_prices.keys()))
        continue

    quantity = int(input("Enter quantity: "))

    price = stock_prices[stock]
    investment = price * quantity

    total_investment += investment

    print("Stock:", stock)
    print("Price:", price)
    print("Quantity:", quantity)
    print("Investment:", investment)

print("\n================================")
print("       PORTFOLIO SUMMARY")
print("================================")
print("Total Investment:", total_investment)
print("================================")