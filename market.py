

import requests

current_exchange=requests.get("https://api.apilayer.com/exchangerates_data/latest",headers={"apikey":"1KgOIE8oesMQjgqsg28TS1JIDsCSWKO3"})
current_exchange=current_exchange.json()
current_exchange=current_exchange['rates']['ILS']

print("Now we will calculate your marketing:\nprices of:\n----------\nTomato=3 NIS\nCucumber=2 NIS\nCola=5 "
      "NIS\nChicken=20 NIS\n ")
Tomato = int(input("Enter how many tomato you want to buy\n "))
Cucumber = int(input("Enter how many Cucumber you want to buy\n "))
Colas = int(input("Enter how many Colas you want to buy\n "))
Chicken = int(input("Enter how many Chicken you want to buy\n "))

print("Summary of your orders:\n----------\nTomato:" f'{str(Tomato)}\nCucumber:{str(Cucumber)}\nColas:{str(Colas)}\nChicken:{str(Chicken)} ')

summery = (Tomato*3) + (Cucumber*2) + (Colas*5) + (Chicken*20)
print("yoe need to pay: " f'{str(summery)} NIS without TAX ')
print("yoe need to pay: " f'{str(summery*1.17)} NIS with TAX ')


current = summery * current_exchange
print(current)
print(summery)



