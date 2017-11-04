from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re
import requests
import json
from coinmarketcap import Market
from .config import coins
def get_coin(coin=None):
    """ Get Price of Coin by USD """
    for i in coins:
        if coin.upper() == i['symbol']:
            coinmarketcap = Market()
            coin_info = coinmarketcap.ticker(currency=i['id'], convert='USD')
            return coin_info[0]
    return None
@listen_to('get (.*)', re.IGNORECASE)
def reply(message, coin=None):
    coin_info = get_coin(coin=coin)
    if coin_info is None:
        msg = "Coinbot does not support this currency"
        message.reply(msg)
    else:
        msg = "1 " + coin_info['symbol'] + " = " + coin_info['price_usd'] + " USD"
        message.reply(msg)
        msg = "Percent Change 1 h :`" + coin_info['percent_change_1h'] +  "` %"
        message.reply(msg)
        msg = "Percent Change 24 h :`" + coin_info['percent_change_24h'] +  "` %"
        message.reply(msg)