import requests


class Stock:
    def __init__(self, symbol: str = ""):
        self.symbol = symbol

    def get_stock_price(self):
        """Uses Financial Modelling API to get real stock price."""
        price = None
        url = "https://financialmodelingprep.com/api/v3/quote-short/{symbol}".format(symbol=self.symbol)
        params = {
            'apikey': "c13a5d2ecf7cc6b8c50c06d7e1dfce22"
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            if len(response.json()) > 0:
                price = response.json()[0].get("price")
        return price
