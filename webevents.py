from flask import Flask,request,json,Response

class ApiGetter:
	app = Flask(__name__)
	users = {}
	users_change = [False]

	@app.route('/')
	def hello_world():
		return 'Hello World!'

	@app.route('/jarvis/dota', methods = ['GET','PUT','DELETE','POST'])
	def add_player_to_queue():
		#users=ApiGetter.users
		#if request.headers['Content-Type'] == 'application/json':
		if request.method=='GET':
			return Response(json.dumps(ApiGetter.users.values()),status=200,mimetype='application/json')

		elif request.method=='POST':
			reqjson=request.get_json()
			userid= reqjson['Userid']
			if ApiGetter.users.has_key(userid):
				return 'Already in queue'
			else:
				ApiGetter.users[userid]=reqjson
				ApiGetter.users_change[0]=True
				return Response(status=200,mimetype='application/json')

		elif request.method=='PUT':
			reqjson=request.get_json()
			userid= reqjson['Userid']
			if ApiGetter.users.has_key(userid):
				ApiGetter.users[userid]=reqjson
				ApiGetter.users_change[0]=True
				return Response(status=200,mimetype='application/json')
			else:
				return 'User not in queue'
			
		elif request.method=='DELETE':
			reqjson=request.get_json()
			userid= reqjson['Userid']
			if ApiGetter.users.has_key(userid):
				del ApiGetter.users[userid]
				ApiGetter.users_change[0]=True
				return Response(status=200,mimetype='application/json')
			else:
				return 'User not in queue'

		#else:
		#	return Response(status=415,mimetype='application/json')

	def run(self):
		self.app.run()

	#def flip_changes():
	#	users_change= not users_change 

	#def user_mutate():
	#	return users_change

	#def users_value():
	#	return ApiGetter.users.values()

#if __name__ == '__main__':
#	app.run()




