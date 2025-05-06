import requests

def main():
    api_key = "d49b10dfe4da45a4a3f180843252702"
    location = input("Please select a City, State, or ZIP code: ")
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}"
    # alerts_url = f"https://api.weatherapi.com/v1/alerts.json?key={api_key}&q={location}"
    # http://api.weatherapi.com/v1/current.json?key=d49b10dfe4da45a4a3f180843252702&Q=London
    response = requests.get(url)
    # alerts_response = requests.get(alerts_url)

    if response.status_code == 200:
        data = response.json()
        last_update = data['current']['last_updated']
        location_name = data['location']['name']
        region = data['location']['region']
        country = data['location']['country']
        temp_f = data['current']['temp_f']
        condition = data['current']["condition"]['text']
        feels_like = data['current']['feelslike_f']
        wind_mph = data['current']['wind_mph']
        wind_dir = data['current']['wind_dir']
        humidity = data['current']['humidity']

        print(f"Last Updated - {last_update}")
        print(f"Location - {location_name}")
        if country == "United States of America" or country == "USA":
            print(f"State - {region}")
        else:
            print(f"Region - {region}")
        print(f"Country - {country}")
        print(f"Temperature - {temp_f}")
        print(f"Conditions - {condition}")
        print(f"Feels like - {feels_like}")
        print(f"Humidity level - {humidity}")
        print(f"Wind Speed - {wind_mph}")
        print(f"Wind direction - {wind_dir}")

    else:
        print(f"Error: {response.status_code}")

    # if alerts_response.status_code == 200:
    #     alerts_data = alerts_response.json()
    #     print(alerts_data)  # Debug print to check the structure of alerts_data
    #     if 'alerts' in alerts_data and alerts_data['alerts']:
    #         for alert in alerts_data['alerts']:
    #             print(alert)  # Debug print to check the structure of each alert
    #             headline = alert['headline']
    #             print(f"News - {headline}")
    # else:
    #     print(f"Error: {alerts_response.status_code}")

if __name__ == "__main__":
    main()