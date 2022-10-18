import requests

api = "http://api.openweathermap.org/data/2.5/weather?appid=3ab4d5b80b129d329c2c5d9d83dae018&q="


def fahrenheit(k_temp):
    return round(((9 / 5) * (k_temp - 273.15)) + 32)


def celsius(k_temp):
    return round(k_temp - 273.15)


print("Welcome to my weather reporting app!\n")

loop = True
while loop is True:
    print("For a simple weather report, please type '1'.\n")
    print("To access advanced weather data, please type '2'.\n")
    print("For more information on simple weather reports and advanced weather data, please type '3'\n")
    report_type = input()
    if report_type == "1":
        simple_loop = True
        while simple_loop is True:
            print("Please type the name of any city, worldwide. (input is not case-sensitive)")
            key = input()
            address = api + key
            response = requests.get(address).json()
            if response:
                try:
                    response['main']['temp']
                    pass
                except KeyError:
                    print(f"{key} not found. Please try again!\n")
                    continue
            simple_loop = False
            address = api + key
            response = requests.get(address).json()
            k_current = fahrenheit(response['main']['temp'])
            k_feel = fahrenheit(response['main']['feels_like'])
            k_high = fahrenheit(response['main']['temp_max'])
            k_low = fahrenheit(response['main']['temp_min'])
            full_description = response['weather'][0]['description']
            print(f"The description of today's weather in {key} is: {full_description}.\n"
                  f"The current temperature in {key} is {k_current}°F and it feels like {k_feel}°F.\n"
                  f"The high temperature in {key} today is {k_high}°F and the low is {k_low}°F.\n")
            cont_loop = True
            print("Please enter 1 to return to the main menu or enter 2 to exit.\n")
            while cont_loop is True:
                cont = input()
                if cont == "2":
                    cont_loop = False
                    loop = False
                    print("Thank you for learning about today's weather with me!")
                    exit()
                elif cont == "1":
                    cont_loop = False
                    continue
                elif cont != "1" and cont != "2":
                    print(f"{cont} is not a valid input. Please try again.")
                    continue

    if report_type == "2":
        advanced = True
        while advanced is True:
            print("You have accessed the advanced features. Please begin by entering the name of any city, worldwide. (input is not case-sensitive)")
            key = input()
            address = api + key
            response = requests.get(address).json()
            if response:
                try:
                    response['main']['temp']
                    pass
                except KeyError:
                    print(f"{key} not found. Please try again!\n")
                    continue
            response = requests.get(address).json()
            k_current = fahrenheit(response['main']['temp'])
            k_feel = fahrenheit(response['main']['feels_like'])
            k_high = fahrenheit(response['main']['temp_max'])
            k_low = fahrenheit(response['main']['temp_min'])
            c_current = celsius(response['main']['temp'])
            c_feel = celsius(response['main']['feels_like'])
            c_high = celsius(response['main']['temp_max'])
            c_low = celsius(response['main']['temp_min'])
            full_description = response['weather'][0]['description']
            humidity = response['main']['humidity']
            wind = response['wind']['speed']
            wind_mph = round(wind * 2.23694)
            visibility = response['visibility']
            temp_loop = True
            restart_adv = False
            while temp_loop is True:
                print("Please input 1 for results in Celsius or input 2 for results in Fahrenheit.")
                measurement = input()
                if measurement == "1":
                    print("You have selected Celsius.\n")
                    temp_loop = False
                if measurement == "2":
                    print("You have selected Fahrenheit.\n")
                    temp_loop = False
                if measurement != "1" and measurement != "2":
                    print(f"{measurement} is not a valid input. Please try again!")
                    continue
                unit = "0"
                if measurement == "1":
                    unit = "1"
                elif measurement == "2":
                    unit = "2"
                command_loop = True
                while command_loop is True:
                    print("You may now enter any valid command to access advanced weather data. For a full list of commands, input '0'")
                    command = input()
                    if command == "0":
                        print(f"1 = Current weather description in {key}.\n"
                              f"2 = Current temperature in {key}.\n"
                              f"3 = What the current temperature feels like in {key}.\n"
                              f"4 = The daily high temperature in {key}.\n"
                              f"5 = The daily low temperature in {key}.\n"
                              f"6 = The humidity in {key}.\n"
                              f"7 = Today's wind speed in MPH in {key}.\n"
                              f"8 = Swaps between results in celsius and fahrenheit.\n"
                              f"9 = Returns to the beginning of the advanced data, allowing you to change cities.\n"
                              f"10 = Returns to the beginning of the program, allowing you to access simple weather reports and the tutorial.\n"
                              f"11 = Exits the program.\n")
                        continue
                    elif command == "1":
                        print(f"The description of the current weather in {key} is {full_description}.\n")
                        continue
                    elif command == "2":
                        if unit == "1":
                            print(f"The current temperature in {key} is {c_current}°C.\n")
                        else:
                            print(f"The current temperature in {key} is {k_current}°F.\n")
                        continue
                    elif command == "3":
                        if unit == "1":
                            print(f"The current temperature in {key} is {c_feel}°C.\n")
                        else:
                            print(f"The current temperature in {key} is {k_feel}°F.\n")
                        continue
                    elif command == "4":
                        if unit == "1":
                            print(f"The current temperature in {key} is {c_high}°C.\n")
                        else:
                            print(f"The current temperature in {key} is {k_high}°F.\n")
                        continue
                    elif command == "5":
                        if unit == "1":
                            print(f"The current temperature in {key} is {c_low}°C.\n")
                        else:
                            print(f"The current temperature in {key} is {k_low}°F.\n")
                        continue
                    elif command == "6":
                        print(f"The current humidity in {key} is {humidity}.\n")
                        continue
                    elif command == "7":
                        print(f"Today's wind speed in {key} is {wind_mph} MPH.\n")
                        continue
                    elif command == "8":
                        temp_loop = True
                        command_loop = False
                        continue
                    elif command == "9":
                        temp_loop = False
                        command_loop = False
                        restart_adv = True
                    elif command == "10":
                        temp_loop = False
                        command_loop = False
                        restart_adv = False
                        advanced = False
                    elif command == "11":
                        print("Thank you for learning about weather data today!")
                        exit()
                    else:
                        print(f"{command} is not a valid input, please try again!")
                        continue

    if report_type == "3":
        report_loop = True
        while report_loop is True:
            print("Please input 1 to learn about simple weather reports, input 2 to learn about advanced weather data,\ninput 3 to go back to the main menu, or input 4 to exit.\n")
            info_type = input()
            if info_type == "1":
                print("Simple weather reports will ask you to input a city, and in return we will give you:\n"
                      "a description of the weather, as well as the 'feels like', current, high, and low temperature in Fahrenheit for the day.\n")
                continue
            elif info_type == "2":
                print("Accessing advanced weather data allows you to retrieve:\n"
                "a city's wind speed in MPH, humidity, weather description, and temperature information Celsius or Fahrenheit\n"
                "This allows you to get more precise weather data, but requires more effort than generating simple weather report.\n")
                continue
            elif info_type == "3":
                report_loop = False
            elif info_type == "4":
                "Thank you for learning about weather data with me today!"
                exit()

            elif info_type != "1" and info_type != "2" and info_type != "3" and info_type != "4":
                print(f"{info_type} is not a valid input. Please try again\n")
                continue
        continue

    if report_type != "1" and report_type != "2" and report_type != "3":
        print("This is not a valid input, please try again.\n")
        continue
    continue
