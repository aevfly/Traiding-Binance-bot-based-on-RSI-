# Traiding-Binance-bot-based-on-RSI-

This repository contains a simple trading bot that uses Binance API to buy and sell cryptocurrencies based on the Relative Strength Index (RSI) indicator. The bot trades the cryptocurrency pair BTCUSDT on the 15m timeframe, using historical data from the last 30 days.
Installation

To run the bot, you need to have Python 3 and the following libraries installed:

    numpy
    binance
    requests
    talib

## You can install these libraries using pip:

```
pip install numpy binance requests talib
```

## Configuration

Before running the bot, you need to set your Binance API key and secret. You can obtain these keys from your Binance account.

Replace the placeholders <api_key> and <api_secret> in the following line of the main() function with your actual API key and secret, respectively:

python
```
client = Client('<api_key>', '<api_secret>')
```

## Usage

To run the bot, simply execute the main() function:
```
python bot.py
```

The bot will start searching for trading signals based on the RSI indicator. When the RSI falls below 30, the bot will place a buy order for the specified quantity at the current market price. When the RSI rises above 70, the bot will place a sell order for the same quantity at the current market price.

The bot will print the RSI value, the order type (buy or sell), and the order details when a trade is executed.

The buy and sell flags are used to prevent the bot from placing multiple orders in a row. Once a buy order is placed, the buy flag is set to True, and the bot will wait for an sell signal before placing another buy order. The same applies to sell orders.

The total variable is used to keep track of the portfolio value. The bot starts with a total of 50000 USDT and updates the value after each trade based on the current BTC price. The btc and usd variables keep track of the BTC and USDT balance, respectively.

The bot runs in an infinite loop and checks for trading signals every second. You can stop the bot at any time by pressing Ctrl-C.
## Disclaimer

This trading bot is provided for educational and informational purposes only. It should not be used for real trading without thorough testing and backtesting. Trading cryptocurrencies carries a high level of risk and may result in significant financial losses. The author of this bot is not responsible for any losses incurred while using this bot.
