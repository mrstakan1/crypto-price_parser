import requests

def get_crypto_price(ticker):
    ticker = ticker.lower()
    try:
        req = requests.get(f"https://yobit.net/api/3/ticker/{ticker}_usd")
        response = req.json()
        sell_price = response[f"{ticker}_usd"]["sell"]
        return sell_price
    except Exception as exception:
        print(exception)
        return False

print(get_crypto_price('btc'))