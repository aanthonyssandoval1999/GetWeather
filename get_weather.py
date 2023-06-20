#DONE
import requests

# OpenWeatherMap API key
API_KEY = "*Hidden*"

# Function to fetch weather data from OpenWeatherMap API
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        main_info = data["weather"][0]["main"]
        description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        weather_info = f"Weather in {city}:\n\n" \
                       f"Sky: {main_info}\n" \
                       f"Description: {description}\n" \
                       f"Temperature: {temperature * 1.8 + 32}°F\n" \
                       f"Humidity: {humidity}%\n" \
                       f"Wind Speed: {wind_speed} m/s"

        return weather_info
    else:
        error_message = data["message"]
        return f"Error: {error_message}"

# Prompt the user to enter a city
city = input("Enter a city name: ")

# Get the weather information for the city
weather = get_weather(city)

# Print the weather information
print(weather)
