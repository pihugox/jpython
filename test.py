from webevents import ApiGetter
from steamapi import SteamApi
import threading

api = ApiGetter()
steamapi = SteamApi()

def worker(api):
	api.run()

t=threading.Thread(target=worker,args=(api,))
t.daemon = True
t.start()

###Comunicacion con el api de steam ########

#ejemplos de como obtener datos de dota

#Match_history, parametros (steamid, numero de matches)
res=steamapi.GetMatchHistory('115601790',2)
#print(res)

listadematchs = []
#iteracion sobre la respuesta para obtener los match_ids
for matches in res['result']['matches']:
	listadematchs.append(matches['match_id'])
	print(matches['match_id'])

##Match_details, parametros (matchid)
##matchdetail de los matchids anteriormente obtenidos
for matchid in listadematchs:
	r = steamapi.GetMatchDetails(matchid)
	print(r)
############################################


####Comunicacion con los eventos de la WEB #####

users = api.users
while True:
	#Bucle que determina cuando un jugador se 
	#agrega,elimina, actualiza de la lista de emparejamiento
	while not api.users_change[0]:
		pass
	api.users_change[0] = False

	#ACA IRIA EL CODIGO, en este caso solo imprime la lista actualizada
	#la variable users, contiene toda la info que viene de la web 
	#{userid,steamid,primaryrol,secondaryrol,buy_in, etc}
	#deberia tener una lista solo de cambios para que sea mas rapido (por mejorar)
	print(users.values())

###########################################