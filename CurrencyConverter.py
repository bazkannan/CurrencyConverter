import xml.etree.ElementTree as ET

# Get the data from the Project, Data folder
# Have the XML file, want to get each of this line. Key and value
# Data-type it can be.
# Put every single line into a dictionary then into a list
# You must provide the user with a command line User Interface that allows them to convert an amount from
# one currency to another (where one currency is Euros). Use the daily rate XML file.
# Create an empty list
# XML has root tags and child tags
# Just read the parent and then test this
# Use full file path when parsing data
# Come to the parent, jump to the child. Inside child you have attribute currency and rate
# Collect those data and put it inside item variable and create my own dictionary
# push every single item inside currency
# What is your current currency? Amount ==> 100 Pound ===> 125
# Find currency
# Did 75% of the project
# What is your currency? How much is it? Multiply and show it to you
# If you wanna pass, check variable names and function names.
# Best practice for code
# Create a currency converter app.
# Use the XML file containing the data. This is done
# Provide the user with a User interface that allows them to convert an amount from one currency
# to another (One currency is Euros).
# Use while loop and dictionary, empty list.

import xml.etree.ElementTree as ET

# This method will fetch the data from the XML file. We return the list of currencies and rates.


def get_data():
    currency_list = []  # Empty currency list
    tree = ET.parse("/Users/Bharath/PycharmProjects/FDMTraining/Project/data/data.xml")
    root = tree.getroot()
    for child in root:
        item = {"currency": child.attrib['currency'],
                "rate": child.attrib['rate']}
        currency_list.append(item)

    return currency_list


def find_currency(currency):

    global exchange_rate   # Declared exchange rate as a global variable to ensure it works and accessible in program
    for item in get_data():
        if item['currency'] == currency.upper():
            exchange_rate = item['currency'], item['rate']
            
    return exchange_rate


def convert_euro_to_other():

    # This method will prompt user to enter an amount in Euros first before selecting currency
    try:
        amount_input = float(input("Enter the amount in Euros you wish to convert: "))
        currency_input = input("Which currency do you want to convert to: ")
        convert = find_currency(currency_input)  # Finding the exchange rate from the findCurrency() method
        currency, exchange_rate = convert
        # Finding the currency and the rate so we can return this to the output
        amount_output = (float(amount_input)/float(exchange_rate))  # Calculation to convert the amount with ER
        print(amount_input, "EUR", "=", round(amount_output, 2), currency)  # Display result of conversion
        print("Conversion complete.")
        return amount_output
    except:
        print("Invalid Amount / Currency Code! Please try again. \n")
        pass


def convert_to_euro():

    # This method will prompt user to enter currency and the amount they want to convert
    try:
        currency_input = input("Which currency do you want to enter: ")
        amount_input = float(input("Enter the amount you wish to convert: "))
        convert = find_currency(currency_input)  # Referring to the findCurrency() method using the input value
        exchange_rate = convert[1]  # Finding the exchange rate in the list.
        amount_output = float(amount_input)*float(exchange_rate)
        # Calculation to convert amount of currency to EUR
        print(amount_input, currency_input, "=", round(amount_output, 2), "EUR")  # Display result of conversion
        print("Conversion complete.")
        return amount_output
    except:
        print("Invalid Amount / Currency Code! Please try again. \n")
        pass


def list_currencies():
    for item in get_data():
        print("Currency: ", item["currency"], "\tRate: ", item["rate"])
        # Listing all the currencies along with their rates


def start_menu():

    # Doing a start menu which will prompt the user to open the application.
    # If yes, it proceeds to the menu. Otherwise it terminates
    open_menu = input("Welcome to the Currency Converter Application! \nWould you like to see the list of options "
                      "available to you? (Y/N): \n")
    if open_menu == "y" or open_menu == "Y" or open_menu == "Yes":
        main_menu()
    else:
        print("The application has terminated. ")


def main_menu():

    # While loop is used to ensure that the menu is constantly running until user decides to exit the application.

    running_menu = True
    while running_menu:

        try:
            user_choice = int(input("Select options (1-4): \n1) Convert Euro to other currencies \n2) Convert currency of "
                                "your choice to Euro \n3) List all currencies and rates \n4) Exit Application \n"))
            print(user_choice)

            if user_choice == 1:
                convert_euro_to_other()
            
            if user_choice == 2:
                convert_to_euro()

            if user_choice == 3:
                print(list_currencies())

            if user_choice == 4:
                exit_choice = input("Are you sure you want to close the application? (Y/N): \n")
                if exit_choice == "Y" or exit_choice == "y" or exit_choice == "Yes":
                    print("The application has terminated.")
                    running_menu = False

            if user_choice > 4 or user_choice <= 0:
                print("You have entered invalid selection. Please enter a number between 1-4. \n")
        except:
            print("Please enter an integer. \n")
            pass


start_menu()

# Application will begin with the startMenu() method before proceeding.
# This is the menu layout.
# menu = "selecting options"
#     1. convert from euro to any currency
#     2. convert any currency to euro
#     3. list of currency
#     4. exit
