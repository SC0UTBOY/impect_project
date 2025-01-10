class Stock:
    def __init__(self, symbol, quantity, price):
        self.symbol = symbol  # Stock symbol (e.g., AAPL, GOOGL)
        self.quantity = quantity  # Number of shares
        self.price = price  # Current price per share

    def value(self):
        return self.quantity * self.price  # Total value of the stock

    def __str__(self):
        return f"{self.symbol}: {self.quantity} shares @ ${self.price:.2f} each (Total: ${self.value():.2f})"


class Portfolio:
    def __init__(self):
        self.stocks = {}  # Dictionary to store stocks (key: symbol, value: Stock object)

    def add_stock(self, symbol, quantity, price):
        if symbol in self.stocks:
            # If the stock already exists, update the quantity and price
            existing_stock = self.stocks[symbol]
            existing_stock.quantity += quantity
            existing_stock.price = price  # Update to the latest price
        else:
            # If the stock is new, add it to the portfolio
            self.stocks[symbol] = Stock(symbol, quantity, price)

    def remove_stock(self, symbol):
        if symbol in self.stocks:
            del self.stocks[symbol]
            print(f"Removed {symbol} from the portfolio.")
        else:
            print(f"{symbol} not found in the portfolio.")

    def total_value(self):
        return sum(stock.value() for stock in self.stocks.values())

    def display_portfolio(self):
        if not self.stocks:
            print("Portfolio is empty.")
        else:
            print("Portfolio:")
            for stock in self.stocks.values():
                print(stock)
            print(f"Total Portfolio Value: ${self.total_value():.2f}")


# Example Usage
if __name__ == "__main__":
    portfolio = Portfolio()

    # Add stocks to the portfolio
    portfolio.add_stock("AAPL", 10, 150.50)
    portfolio.add_stock("GOOGL", 5, 2800.00)
    portfolio.add_stock("TSLA", 2, 700.00)

    # Display the portfolio
    portfolio.display_portfolio()

    # Remove a stock
    portfolio.remove_stock("TSLA")

    # Display the updated portfolio
    portfolio.display_portfolio()

    # Add more shares of an existing stock
    portfolio.add_stock("AAPL", 5, 155.00)

    # Display the final portfolio
    portfolio.display_portfolio()