import time
import datetime
import json, requests
from dateutil.parser import parse

def parseExchange(exchange):
	return '\t'+str(data[exchange]['rates']['ask'])+'\t'+str(data[exchange]['rates']['bid'])+'\t'+str(data[exchange]['rates']['last'])+'\t'+str(data[exchange]['volume_btc'])+'\t'+str(data[exchange]['volume_percent'])


while True:
	with open('btc-data.txt', 'a') as f:
		try:
			resp = requests.get(url="https://api.bitcoinaverage.com/exchanges/USD")	
		except requests.exceptions.RequestException as e:
			print e
		else:
			data = json.loads(resp.text)
			dt = parse(data['timestamp'])
			unixtime = int(time.mktime(dt.timetuple()))
			print(datetime.datetime.fromtimestamp(unixtime).strftime('%d-%m-%Y -- %H:%M:%S'))
			line = str(unixtime)
			# line += parseExchange('bitex')
			line += parseExchange('bitfinex')
			line += parseExchange('bitkonan')
			line += parseExchange('bitstamp')
			line += parseExchange('btce')
			# line += parseExchange('campbx')
			line += parseExchange('coinbase')
			# line += parseExchange('coinsetter')
			# line += parseExchange('cointrader')
			# line += parseExchange('cryptonit')
			# line += parseExchange('hitbtc')
			# line += parseExchange('itbit')
			line += parseExchange('kraken')
			line += parseExchange('localbitcoins')
			# line += parseExchange('loyalbit')
			line += parseExchange('okcoinintl')
			# line += parseExchange('rocktrading')
			f.write(line+'\n')
			print(line+'\n--\n')
			time.sleep(6);

