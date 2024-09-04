from config import *
from pybit.unified_trading import HTTP


def format_number(input_string):
    
    number = input_string
    
    formatted_number = f"{number:,}".replace(",", " ")
    return formatted_number


def get(el):
    session = HTTP()
    
    SYMBOL = f"{el}USDT"

    TICKER = session.get_tickers(
    	category="spot",
    	symbol=SYMBOL)['result']['list'][0]

    price = format_number(float(TICKER['lastPrice']))
    highPrice24h = format_number(float(TICKER['highPrice24h']))
    lowPrice24h = format_number(float(TICKER['lowPrice24h']))
        
    return {"Name":el, "Price": f"{price} $", "High":f"{highPrice24h} $", "Low":f"{lowPrice24h} $"}
