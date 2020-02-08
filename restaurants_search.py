# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    restaurants_search.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: HoangPham <HoangPham@student.42.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/03 16:30:49 by hopham            #+#    #+#              #
#    Updated: 2020/02/08 18:36:39 by HoangPham        ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from flask import Flask, jsonify, request
import json
import math

app = Flask(__name__)

def distance(origin, destination):
	lat1 = origin[1]
	lon1 = origin[0]
	lat2 = destination[1]
	lon2 = destination[0]
	radius = 6373.0

	dlat = math.radians(lat2 - lat1)
	dlon = math.radians(lon2 - lon1)
	a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
		math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
		math.sin(dlon / 2) * math.sin(dlon / 2))
	c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
	d = radius * c
	return d

@app.route("/restaurants/search", methods=['GET'])

def show():
	restaurants = list()
	q = request.args.get('q')
	lat = float(request.args.get('lat'))
	lon = float(request.args.get('lon'))
	destination = [lon, lat]

	with open('./restaurants.json', 'r') as f:
		data = json.load(f)
		for res in data["restaurants"]:
			if q in res['name'] or q in res['tags'] or q in res['description']:
				res_pos = res['location']
				res_dis = distance(res_pos, destination)
				if res_dis < 3:
					restaurants.append(res)
			elif len(q) == 0:
				res_pos = res['location']
				res_dis = distance(res_pos, destination)
				if res_dis < 3:
					restaurants.append(res)
	return jsonify(restaurants)

if __name__ == "__main__":
	app.run(debug=True)
