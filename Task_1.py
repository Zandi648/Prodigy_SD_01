temp = float(input("What is your temperature?: "))
unit = input("Is this temperature in Celsius, Fahrenheit or Kelvin (C/F/K)?: ")

if unit.upper() == "C":
    result = (temp * 1.8) + 32
    result2 = temp + 273.15
    print(f"The temperature in Fahrenheit is: {round(result, 2)}°F")
    print(f"The temperature in Kelvin is: {round(result2, 2)}K")

elif unit.upper() == "F":
    result = (temp - 32) / 1.8
    result2 = ((temp - 32) / 1.8) + 273.15
    print(f"The temperature in Celsius is: {round(result, 2)}°C")
    print(f"The temperature in Kelvin is: {round(result2, 2)} K")

elif unit.upper() == "K":
    result = temp - 273.15
    result2 = (((temp - 273.15) * 1.8) + 32)
    print(f"The temperature in Celsius is: {round(result, 2)}°C")
    print(f"The temperature in Fahrenheit is: {round(result2, 2)}°F")

else:
    print(f"{unit}: Please enter a valid unit!")