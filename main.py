import requests

response = requests.get("https://www.ceneo.pl/96796516#tab=reviews")
print(response.text)