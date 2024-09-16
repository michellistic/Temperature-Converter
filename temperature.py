# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    # Formula: (°C × 9/5) + 32 = °F
    return (celsius * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    # Formula: (°F − 32) × 5/9 = °C
    return (fahrenheit - 32) * 5/9

# Main function to handle the temperature conversion process
def temperature_converter():
    # Display a menu with options for the user
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    
    # Get the user's choice (either 1 or 2) for the conversion
    choice = input("Choose the conversion (1/2): ")
    
    # If the user chooses option 1: Celsius to Fahrenheit
    if choice == '1':
        # Ask the user for the temperature in Celsius
        celsius = float(input("Enter temperature in Celsius: "))
        
        # Call the celsius_to_fahrenheit function to convert it
        fahrenheit = celsius_to_fahrenheit(celsius)
        
        # Print the result, formatted to 2 decimal places
        print(f"{celsius}°C is {fahrenheit:.2f}°F")
    
    # If the user chooses option 2: Fahrenheit to Celsius
    elif choice == '2':
        # Ask the user for the temperature in Fahrenheit
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        
        # Call the fahrenheit_to_celsius function to convert it
        celsius = fahrenheit_to_celsius(fahrenheit)
        
        # Print the result, formatted to 2 decimal places
        print(f"{fahrenheit}°F is {celsius:.2f}°C")
    
    # If the user enters an invalid option (not 1 or 2)
    else:
        # Inform the user that their choice is invalid
        print("Invalid choice. Please choose 1 or 2.")

# Call the temperature_converter function to run the program
temperature_converter()
