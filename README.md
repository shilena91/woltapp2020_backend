# woltapp2020_backend
Internship pre-assignment for Wolt's backend developer summer 2020
I started to do this assignment after 1 week of learning python. It's probably not the best solution, but it does what the assignment requires. In case length of query string is 0, I decided to return all restaurants which have location closer than 3km to customer's locations.

## Usage
I did this assignment on MacOS X and by python3. I hope you have same system :D\
Clone the repo or download and unzip the file.\
Install Flask in terminal:
> pip3 install Flask

Run file **_restaurants_search.py_** in terminal:
> python3 restaurants_search.py

Go to any web browser and run following:
> localhost:5000/restaurants/search?q=query_string&lat=latitude&lon=longtitude

Replace _query_string_ as string you want to search, _latitude_ and _longtitude_ as customer's coordinates. It should show a list of restaurants match the string and closer than 3km.

## How I come to the solution
After learning python basics, I started searching on google "create API in python". Most searching results were Flask. That's how I came up with Flask. I still do not have deep knowledge about web development, API and related stuffs.
Anyways this was interesting assignment. I learnt about Flask and how to fetch json data in python, which I think I would definitely use in future.
