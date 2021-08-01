#Zachary Dahir
#Assignment 8.3
#7-28-21

import requests, json

def main():
    apiKey = '25a8bf00b11974c7afaa326f12cea38c'
    dataType = input('Select search method: \n [1] Zipcode \n [2] City \n')

    def veiwLocation():
        if dataType == str(1):
            zip = input('Please enter 5 digit zipcode: \n')

            if len(str(zip)) == 5:
                url = 'http://api.openweathermap.org/data/2.5/weather?zip=' + zip + '&appid=' + apiKey
                response = requests.get(url)
                x = response.json()
                print(x)
        
            else:
                print('Invalid zipcode')
                veiwLocation()

        elif dataType == str(2):
            city = input('Please enter city name:\n')
            url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city +  '&appid=' + apiKey
            response = requests.get(url)
            x = response.json()
            print(x)

        else:
            print('Invalid input')
            veiwLocation()
            
    veiwLocation()

    runAgain = input('Would you like to veiw another location? Yes or No? \n')

    if runAgain == 'Yes' or runAgain == 'yes':
        main()

    else:
        print('Goodbye!')

main()