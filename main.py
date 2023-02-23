import numpy as np
from binance.client import Client
import requests
import talib
import time

SYMBOL = 'BTCUSDT'
INTERVAL = '15m'
LIMIT = '200'
quantity = 24000


client = Client('<api_key>', '<api_secret>')

# Retrieve the historical data
klines = client.get_historical_klines(SYMBOL, INTERVAL, '30 days ago')

# Parse the data
close_prices = []
for kline in klines:
    close_price = float(kline[4])
    close_prices.append(close_price)

close_prices = np.array(close_prices)

def place_order(order_type, symbol, quantity, price=None):
    try:
        if order_type == 'buy':
            order = client.create_order(
                symbol=symbol,
                side=order_type,
                type='MARKET',
                quantity=quantity,
                price=price
            )
            
            print('order ', order)
        elif order_type == 'sell':
            order = client.create_order(
                symbol=symbol,
                side=order_type,
                type='MARKET',
                quantity=quantity,
                price=price
            )
            print('order ', order)
        else:
            raise ValueError('Invalid order side. Must be "buy" or "sell".')

        print(f'{order_type.upper()} order placed: {order}')
    except Exception as e:
        print(f'Error placing {order_type} order: {e}')

def main(close_prices):
    buy = False
    sell = True
    total = 50000 # start portfolio quantity $
    btc = 0
    usd = 0

    print('started searching for signal')
    while True:
        kline = client.get_klines(symbol=SYMBOL, interval=INTERVAL, limit=1)
        close_price = float(kline[0][4])
        close_prices = np.append(close_prices, close_price)
        close_prices = close_prices[-int(LIMIT):]

        rsi = talib.RSI(close_prices, 7)[-1]
        print('rsi', rsi)

        if(rsi <= 30 and not buy):
            print('place order buy', close_prices[-1])
            place_order('buy', symbol=SYMBOL, quantity=quantity, price='MARKET')
            buy = not buy
            sell = not sell
            total = total - quantity
            btc = quantity/close_prices[-1]
            print('btc ' , btc)
            print('total ', total)

        if(rsi >= 70 and not sell):
            print('place order sell', close_prices[-1])
            place_order('sell', symbol=SYMBOL, quantity=quantity, price='MARKET')
            buy = not buy
            sell = not sell
            usd = btc*close_prices[-1]
            total = total + usd
            print('usd ', usd)
            print('total ', total) 


        time.sleep(1)

if __name__ == '__main__':
    main(close_prices)
