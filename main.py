from stock import Stock


AVAILABLE_STOCKS = [
    "AAPL",
    "GOOGL",
    "AMZN",
    "TSLA",
    "FB",
    "TWTR",
    "UBER",
    "LYFT",
    "SNAP",
    "SHOP"
]


def get_stocks_prices() -> dict:
    prices = {}
    for symbol in AVAILABLE_STOCKS:
        stock = Stock(symbol=symbol)
        prices[symbol] = stock.get_stock_price()
    return prices

