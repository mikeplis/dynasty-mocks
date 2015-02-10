from bs4 import BeautifulSoup
import urllib2

urls = [
  'http://football21.myfantasyleague.com/2015/options?L=46044&O=17',
  'http://football21.myfantasyleague.com/2015/options?L=26815&O=17',
  'http://football21.myfantasyleague.com/2015/options?L=38385&O=17',
  'http://football21.myfantasyleague.com/2015/options?L=59370&O=17',
  'http://football21.myfantasyleague.com/2015/options?L=49255&O=17',
  'http://football21.myfantasyleague.com/2015/options?L=45505&O=17'
]

data = {}

for url in urls:
  soup = BeautifulSoup(urllib2.urlopen(url).read())
  rows = soup.find('table', {'class': 'report'}).find_all('tr')
  for row in rows:
    try:
      player = row.find('td', {'class': 'player'}).find('a').text
      dp = int(row.find_all('td', {'class': 'rank'})[1].text.replace('.', ''))
      if player in data:
        dps = data[player]['draft_positions'].append(dp)
        data[player] = {'draft_positions': dps, 'adp': sum(dps)/float(len(dps))}
      else:
        data[player] = {'draft_positions': [dp], 'adp': dp}
    except:
      pass

for player in sorted(data, key=lambda x: data[x]['adp']):
  info = data[player]
  print(player, info['adp'], info['draft_positions'])
