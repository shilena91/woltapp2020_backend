# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    restaurants_search.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hopham <hopham@student.hive.fi>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/03 16:30:49 by hopham            #+#    #+#              #
#    Updated: 2020/02/03 18:43:14 by hopham           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from flask import Flask, jsonify, request
import json
from math import sin, cos, sqrt, atan2, radians

app = Flask(__name__)

def distance(origin, destination):
	lat1 = radians(origin[1])
	lon1 = radians(origin[0])
	lat2 = radians(destination[1])
	lon2 = radians(destination[0])
	radius = 6373.0

	dlon = lon2 - lon1
	dlat = lat2 - lat1
	a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
	c = 2 * atan2(sqrt(a), sqrt(1 - a))
	distance = radius * c
	return (distance)

@app.route("/restaurants/search", methods=['GET'])

def show():
	restaurants = list()
	q = request.args.get('q')
	lat = float(request.args.get('lat'))
	lon = float(request.args.get('lon'))
	destination = [lon, lat]

	with open("./restaurants.json") as f:
		data = json.load(f)
		for res in data["restaurants"]:
			if q in res["name"] or q in res["tags"] or q in res["description"]:
				res_pos = res["location"]
				res_dis = distance(res_pos, destination)
				if res_dis < 3:
					restaurants.append(res)
	return jsonify(restaurants)

if __name__ == "__main__":
	app.run(debug=True)
