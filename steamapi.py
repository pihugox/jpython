import requests

#documentation in http://dev.dota2.com/showthread.php?t=58317

class SteamApi:

	steamkey = 'BD4DCD801E8978DFFDB1C865F39FBC1B'

	def GetMatchHistory(self,steamid,num_matches):
		url = 'https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/v001/'
		parametros = {'key': SteamApi.steamkey,'account_id':steamid,'matches_requested':num_matches}

		return requests.get(url,params=parametros).json()

	def GetMatchDetails(self,match_id):
		url = 'https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/v001/'
		parametros = {'key': SteamApi.steamkey,'match_id':match_id}

		return requests.get(url,params=parametros).json()