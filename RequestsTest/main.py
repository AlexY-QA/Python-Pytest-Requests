import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '68f89133cb9dab5f2b01ff15e20ccad1'
HEADER = {'Content-Type': 'application/json','trainer_token': TOKEN}
body_pokemons = {
    "name": "generate",
    "photo_id": -1
}
response = requests.post(url=f'{URL}/pokemons', headers=HEADER, json = body_pokemons)
print(response)



import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '68f89133cb9dab5f2b01ff15e20ccad1'
HEADER = {'Content-Type': 'application/json','trainer_token': TOKEN}
body_pokemons = {
    "pokemon_id": "334988",
    "name": "Kot",
    "photo_id": 2
}
response = requests.put(url=f'{URL}/pokemons', headers=HEADER, json = body_pokemons)
print(response)


import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '68f89133cb9dab5f2b01ff15e20ccad1'
HEADER = {'Content-Type': 'application/json','trainer_token': TOKEN}
body_pokemons = {
    "pokemon_id": "334988"
}
response = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json = body_pokemons)
print(response)