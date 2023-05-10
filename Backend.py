import flask
from flask import Flask, Response, request, render_template, redirect, url_for
import flask_login
import requests
from requests import post
import json
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def search_game_by_name():
    if request.method == 'POST':
        name = request.form.get('game_name')
        url = "https://rawg-video-games-database.p.rapidapi.com/games/" + name + "?key=2f70e298b9ba477e80cc87048455f30a"

        headers = {
        	"X-RapidAPI-Key": "7740c2a325msh0911c68659b1739p1f47f3jsn641fd99e2bf0",
        	"X-RapidAPI-Host": "rawg-video-games-database.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers)
        y = json.loads(response.text)
        descrip = y
        return render_template('display.html', description = descrip)
    else:
        return render_template('search.html')
        
if __name__ == "__main__":
	#this is invoked when in the shell  you run
	#$ python game-rank-backend.py
	app.run(port = 8888, debug=True)
