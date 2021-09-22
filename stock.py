import json
import pandas as pd
import json
import sqlite3


obj = json.loads('{"AAPL": 142.94,"ORCL": 86.17,"SPY": 434.04}')
print(obj['AAPL'])

import requests

url = "https://rest.yahoofinanceapi.com/v6/finance/quote"
querystring = {"symbols":"AAPL,ORCL"}
headers = {
    'x-api-key': "1MgUriJTmF2t2zZ4FFjpj4pvmf2H2xXLaWagZwh0"
    }
response = requests.request("GET", url, headers=headers, params=querystring)
#print(response.text)
stock_json = response.json()
print(stock_json['quoteResponse']['result'])


