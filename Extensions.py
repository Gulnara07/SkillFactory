import requests
import json
from Config import keys

class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(quote, base, amount):
        if quote == base:
            raise ConvertionException(f"Не удалось перевести одинаковые валюты {quote}")

        try:
            quote_ticker = keys[quote.lower()]
        except KeyError:
            raise ConvertionException(f"Не удалось обработать валюту {quote}")

        try:
            base_ticker = keys[base.lower()]
        except KeyError:
            raise ConvertionException(f"Не удалось обработать валюту {base}")

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f"Не удалось обработать количество {amount}")

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]
        new_price = float(amount) * float(total_base)
        #print(new_price)
        return total_base
        return new_price

