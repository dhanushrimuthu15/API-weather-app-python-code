# Weather API Integration Project

## Project Overview

This project demonstrates API integration using Python and the Requests library. It fetches real-time weather information from the OpenWeather API based on a city entered by the user.

## Features

- Fetches live weather data
- Uses the Requests module
- Parses JSON responses
- Allows users to search by city name
- Displays temperature, humidity, weather description, and wind speed

## Technologies Used

- Python
- Requests Library
- OpenWeather API

## Requirements

- Python 3.x
- Requests

Install the required library:

```bash
python -m pip install requests
```

## How to Run

1. Get an API key from OpenWeather.
2. Replace:

```python
API_KEY = "YOUR_API_KEY"
```

with your own API key.

3. Run:

```bash
python main.py
```

4. Enter a city name.

Example:

```
Enter city name:
Vellore
```

## Sample Output

```
Weather Information
---------------------
City: Vellore
Temperature: 31°C
Humidity: 68%
Weather: scattered clouds
Wind Speed: 2.5 m/s
```

## Project Structure

```
API_Integration_Weather/
│
├── main.py
├── requirements.txt
├── README.md
└── screenshots/
```

## Author

**DHANUSHRI M**