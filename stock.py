import json
import pandas as pd
import json
import sqlite3
import argparse
import requests

#1 Grab a list of quotes to get form Yahoo


parser = argparse.ArgumentParser()

parser.add_argument("-s", "--stock", dest = "stock", default="ORCL", help="Seperated by commas")
args = parser.parse_args()

print("Pulling data for:" + args.stock)

stock= args.stock
apikey="1MgUriJTmF2t2zZ4FFjpj4pvmf2H2xXLaWagZwh0"

#obj = json.loads('{"AAPL": 142.94,"ORCL": 86.17,"SPY": 434.04}')
#print(obj['AAPL'])


url = "https://rest.yahoofinanceapi.com/v6/finance/quote"
querystring = {"symbols":stock}
headers = {
  'x-api-key': apikey
   }
response = requests.request("GET", url, headers=headers, params=querystring)
#print(response.text)
stock_json = response.json()
print(stock_json['quoteResponse']['result'][0]["displayName"] + " Price:$" + str(stock_json['quoteResponse']['result'][0]["regularMarketPrice"]))