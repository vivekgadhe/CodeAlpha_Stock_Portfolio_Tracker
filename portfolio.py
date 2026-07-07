
def calculate_total(portfolio, stock_prices):
    total = 0
    for stock, qty in portfolio.items():
        total += stock_prices[stock] * qty
    return total
