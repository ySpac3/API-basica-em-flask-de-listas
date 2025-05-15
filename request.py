import requests

url = 'http://127.0.0.1:5000/request'

lista = [10,20,30]

resposta2 = requests.post(url, json=lista)

resposta = requests.get(url)

print()

print(resposta.json())