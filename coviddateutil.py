#!/usr/bin/python3


import requests, json 
import unicodedata
from coviddists import get_district_code_from_passing

def covid_data(keyToSearch):
	response = requests.get('https://api.covid19india.org/v2/state_district_wise.json')
	print("RESPONSE", response)
	try:
		covid_data = response.json()
		y = json.dumps(covid_data[1])
		x = json.loads(y)
		districtDataofX=json.dumps(x["districtData"])
		districtDataofXjson = json.loads(districtDataofX)
		json_search_keys = create_filter(keyToSearch)
		print("covid_data--", json_search_keys)
		for k in covid_data:
			covid_states = json.dumps(k)
			covid_states_json = json.loads(covid_states)
			if covid_states_json["statecode"] == json_search_keys[0]:
				for k1 in covid_states_json["districtData"] :
					covid_states_dist = json.dumps(k1)
					covid_states_dist_json = json.loads(covid_states_dist)
					if covid_states_dist_json["district"] == json_search_keys[2]:
						#print("\n\nDistrict data: ",covid_states_dist_json)
						to_str_active = str(covid_states_dist_json["active"])
						to_str_confirmed = str(covid_states_dist_json["confirmed"])
						to_str_deceased = str(covid_states_dist_json["deceased"])
						to_str_recovered = str(covid_states_dist_json["recovered"])
						fin_data = "Cases in "+ covid_states_dist_json["district"]+ ", Confirmed: "+to_str_confirmed+\
							   ", Deceased: "+to_str_deceased+ ", Recovered: "+to_str_recovered+\
							   ", Active: "+to_str_active;
						print (fin_data)
						return fin_data
	except KeyError:
		print("Data error")
		return ": Data error or probably no data for your query"


def create_filter(cmd_string):
	print("Query ->",cmd_string)
	dist = get_dist(cmd_string)
	return dist

def get_dist(dist_code):
	broken = dist_code.split(" ")
	dist = broken[1]
	filter_keys = []
	filter_keys.append(dist[0:2])
	filter_keys.append(dist[2:])
	dist_name = get_district_code_from_passing(broken[1])
	filter_keys.append(dist_name)
	return filter_keys

#covid_data("covid MH12")
