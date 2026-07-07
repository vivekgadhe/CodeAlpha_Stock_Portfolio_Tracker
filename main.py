from portfolio import calculate_total
from prices import stock_prices
import csv

def main():
    portfolio = {}
    while True:
        stock = input("Enter stock symbol (or 'done' to finish): ").upper()
        if stock == "DONE":
            break
        if stock not in stock_prices:
            print("Stock not found in price list!")
            continue
        qty = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + qty

    total = calculate_total(portfolio, stock_prices)
    print(f"\nTotal Investment Value: ${total}")

    # Save to CSV
    with open("results.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Stock", "Quantity", "Price", "Value"])
        for stock, qty in portfolio.items():
            writer.writerow([stock, qty, stock_prices[stock], stock_prices[stock] * qty])
        writer.writerow([])
        writer.writerow(["Total Investment", "", "", total])

if __name__ == "__main__":
    main()
