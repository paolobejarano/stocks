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


def obtener_portafolio(capital: float) -> dict:
    portafolio = {}
    prices = get_stocks_prices()
    for stock in AVAILABLE_STOCKS:
        portafolio[stock] = 0
        if capital > prices[stock]:
            capital -= prices[stock]
            portafolio[stock] = 1
        else:
            break
    prices = sorted(prices.items(), key=lambda x: x[1], reverse=True)
    sorted_prices = {}
    for price in prices:
        sorted_prices[price[0]] = price[1]
    for stock in sorted_prices:
        portafolio[stock] += capital // sorted_prices[stock]
        capital -= sorted_prices[stock] * (capital // sorted_prices[stock])
    return portafolio


print(obtener_portafolio(capital=3000000))
