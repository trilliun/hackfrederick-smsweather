import requests
import pprint

# OpenWeatherMap API
params = {
	'q': 'Frederick,US',
	'appid': '4ce082e5c4e81ec8283fde2f65796473',
	'units' : 'imperial',
}

response = requests.get(
	'http://api.openweathermap.org/data/2.5/weather', params=params)

weather_data = response.json()
# pprint.pprint(weather_data)

# pulls data to use in text message
city = weather_data['name']
temperature = weather_data['main']['temp']
message = 'The weather in {} is {} degrees Fahrenheit.'.format(city, temperature)

# NexMo API
params = {
    'api_key': '116d848a',
    'api_secret': 'd1deb332d3f28425',
    'from': '12132633755',
    'to': '13049953889',
    'text': message,
}
requests.get('https://rest.nexmo.com/sms/json', params=params)