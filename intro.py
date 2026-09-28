# print(64587)
# print("Jakub")
# name = "Kuba"
# print(name)
# age = 22
# country = "Poland"
# dietary = "non-vegetarian"
# print(age, name, country, dietary)
# print("My name is ", name, " and I am ", age, " years old. I live in ", country, " and I am a ", dietary, ".")
# salary = 1000
# business = 700
# income = salary + business
# print("My total income is ", income, " dollars.")
# polish = ['Jakub', 'Kuba', 'Kowalski', 'Nowak', 'Wojcik']
# print(polish)
# age_2 = [20, 22, 25, 30, 35]
# print(age_2 [0])

'''PANDAS'''
import pandas as pd

data = pd.read_csv('/Users/jakubwojciechowski/Library/CloudStorage/OneDrive-AkademiaLeonaKozminskiego/Network and Business Analysis/intro-to-analytics-jw/bitcoin_price_daily.csv')
print(data.head(2))
print(data.describe())