import urllib2
import json
import random
from pprint import pprint
 
import time
import Poloniex
 
CURRENCY = 'XMR'
 
APIKEY = 'YOUR_API_KEY'
SECRET = 'YOUR_API_SECRET'
 
class PoloniexChangeDeposit:
    def __init__(self):
        pass
 
    def run(self):
            poloniex = Poloniex.poloniex(APIKEY, SECRET)
            address = poloniex.newAddress(CURRENCY)
            print address['response']
 	    
if __name__ == "__main__":
    PoloniexChangeDeposit().run()
