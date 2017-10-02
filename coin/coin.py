from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re
import requests
import json
def get_coin(coin=None):
    """ Get Price of Coin by USD """
    url = "https://coinbin.org/" + coin
    r = requests.get(url)
    result = json.loads(r.text)
    return result['coin']['usd']

@listen_to('hi', re.IGNORECASE)
def hi(message):
    message.reply('I can understand hi or HI!')
    # react with thumb up emoji
    message.react('+1')

@listen_to('eth')
def eth(message):
    price = str(get_coin(coin="eth"))
    message.reply('1 ETH = ' + price + " USD")
@listen_to('btc')
def btc(message):
    price = str(get_coin(coin="btc"))
    message.reply('1 BTC = ' + price + " USD")