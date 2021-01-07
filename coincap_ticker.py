import requests

listings_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?convert=INR'

request = requests.get(url=listings_url, headers={'X-CMC_PRO_API_KEY': 'Your_API_Key'})
result = request.json()
data = result['data']

for currency in data:
    rank = currency['id']
    name = currency['name']
    symbol = currency['symbol']

    circulating_supply = currency['circulating_supply']
    total_supply = currency['total_supply']

    market_cap = currency['quote']['INR']['market_cap']
    hour_change = currency['quote']['INR']['percent_change_1h']
    day_change = currency['quote']['INR']['percent_change_24h']
    week_change = currency['quote']['INR']['percent_change_7d']
    price = currency['quote']['INR']['price']
    volume = currency['quote']['INR']['volume_24h']

    volume_string = '{:,}'.format(volume)
    market_cap_string = '{:,}'.format(market_cap)
    circulating_supply_string = '{:,}'.format(circulating_supply)
    total_supply_string = '{:,}'.format(total_supply)

    print(str(rank) + ': ' + name + ' (' + symbol + ')')
    print('Market cap: \t\t\t₹' + market_cap_string)
    print('Price: \t\t\t\t\t₹' + str(price))
    print('24h Volume: \t\t\t₹' + volume_string)
    print('Hour change: \t\t\t' + str(hour_change) + '%')
    print('Day change: \t\t\t' + str(day_change) + '%')
    print('Week change: \t\t\t' + str(week_change) + '%')
    print('Total supply: \t\t\t' + total_supply_string)
    print('Circulating supply: \t' + circulating_supply_string)
    # print('Percentage of coins in circulation: ' + str(int(circulating_supply/total_supply*100)))
    print()
