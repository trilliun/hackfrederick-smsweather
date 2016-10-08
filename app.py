from flask import Flask
from flask import jsonify
import requests
from datetime import datetime

app = Flask(__name__)

def icon(icon_id):
  fullpath = 'http://openweathermap.org/img/w/%s.png' % icon_id
  img = requests.get(fullpath)
  return img

def weather():
  params = {
      'q': 'Frederick, MD',
      'appid': '4ce082e5c4e81ec8283fde2f65796473',
  }

  response = requests.get(
      'http://api.openweathermap.org/data/2.5/weather', params=params)

  weather_data = response.json()
  weather_data['time'] = datetime.now()
  return weather_data

@app.route('/')
def main():
  weather_data = weather()
  return jsonify(weather_data)

@app.route('/image')
def image():
  weather_data = weather()
  image = icon(weather_data['weather'][0]['icon'])
  return Flask.response_class(image, mimetype='image/png')