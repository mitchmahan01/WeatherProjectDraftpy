import json, requests
#Uses api key to search by city for user to find weather#
base_url_by_city = "http://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={api_key}&units=imperial"
#Uses api key to search for location via zip code if they would like to enter the zip instead#
base_url_by_zip = "http://api.openweathermap.org/data/2.5/weather?zip={ZIP_CODE},us&appid={api_key}&units=imperial"
#WeatherApi Key#
api_key = '70d9c51e7360a54d4e27fc8462f05784'
#Uses search method alongside user input to find info from specified location
search_method = input("How would you like to search for weather information? Enter 'city' or 'zip': \n")

if search_method.lower() == 'city':
    city_name = input("Please enter your city name: \n")
    url = base_url_by_city.format(CITY_NAME=city_name, api_key=api_key)
	#Uses city name to retrieve weather info#
	#Uses zip code to retrieve location weather#
elif search_method.lower() == 'zip':
    zip_code = input("Please enter your zip code: \n")
    url = base_url_by_zip.format(ZIP_CODE=zip_code, api_key=api_key)
else:
	#Error message if location is not found#
    print("Invalid search method entered. Please try again.")
    exit()
#prints response based off of elif/else statement above#
print()

response = requests.get(url)
data = response.json()
#Max temp output for specified location#
temp_max = data["main"]["temp_max"]
print(f"The max temp is: {temp_max}")
#Current temp output for specified location#
temp = data["main"]["temp"]
print(f"Current Temp is {temp}")
