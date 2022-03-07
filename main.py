import os
import requests

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')
	
def lookup():
	Token = os.environ['Apex API Key']
	URLP1 = "https://api.mozambiquehe.re/bridge?version=5/&platform="
	URLP2= "&player="
	URLP3= "&auth="
	#inputs
	print("UserName: ")
	UserName=input("")
	print("Platform (PC, PS4, X1): ")
	Platform=input("")

	url=URLP1+(Platform.upper())+URLP2+UserName+URLP3+Token

	#curls
	curl = requests.get(url)

	r_dict = curl.json()

	#interface---------------------------------
	print("\n\n---------------")
	print("-> User ->")
	print(r_dict['global']['name'])
	print("---------------")
	
	print("-> Level -> ")
	print(r_dict['global']['level'])
	print("---------------")
	
	print("-> Rank -> ")
	print(r_dict['global']['rank']['rankScore'],r_dict['global']['rank']	['rankName'], r_dict['global']['rank']['rankDiv'])	
	print("---------------")

	print("-> General Stats ->")
	print("KD: ",r_dict['total']['kd']['value'])
	print("Trackers :")
	try:
		print(r_dict['legends']['selected']['data'][0]['name'],":",r_dict['legends']	['selected']['data'][0]['value'])
	except:
		print("No Slot 1 Tracker")
	try:
		print(r_dict['legends']['selected']['data'][1]['name'],":",r_dict['legends']['selected']['data'][1]['value'])
	except:
		print("No Slot 2 Tracker")
	try:
		print(r_dict['legends']['selected']['data'][2]['name'],":",r_dict['legends']['selected']['data'][2]['value'])
	except:
		print("No Slot 3 Tracker")
	print("---------------")

	print("-> Threat Level (1-10) ->")
	threat = float(r_dict['global']['rank']['rankScore'])/(r_dict['global']['level'])
	multipler = float(r_dict['total']['kd']['value'])
	print(round((multipler*threat)-2))
	
	print("---------------")
	print("Other Stats: ")
	if r_dict['realtime']['isOnline'] == 1:
		print("User Is Online")
	else:
		print("User Is Offline")
	print("User Has",r_dict['realtime']['selectedLegend'],"Selected")

	yn()
def yn():
	print("\n\nSearch A New Player? (Yn): ")
	yesno = input("")
	if yesno.upper() == "Y":
	
		print("Clear Console? (Yn): ")
		yesno = input("")
	
		if yesno.upper() == "Y":
			clear()
			lookup()
		else:
			lookup()

lookup()


