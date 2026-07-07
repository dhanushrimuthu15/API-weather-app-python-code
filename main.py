import requests

# Replace with your OpenWeatherMap API key

API_KEY = "fdf95a45fa44cb0e9742169ab82b5705"

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

try:
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        print("\n------ Weather Report ------")
        print("City:", data["name"])
        print("Country:", data["sys"]["country"])
        print("Temperature:", data["main"]["temp"], "°C")
        print("Humidity:", data["main"]["humidity"], "%")
        print("Weather:", data["weather"][0]["description"])
        print("Wind Speed:", data["wind"]["speed"], "m/s")
    else:
        print("\nError:", data.get("message", "Unable to fetch weather data."))

except Exception as e:
    print("An error occurred:", e)