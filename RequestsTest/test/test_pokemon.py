import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '68f89133cb9dab5f2b01ff15e20ccad1'
HEADER = {'Content-Type': 'application/json','trainer_token': TOKEN}
TRAINER_ID = '34224'

def test_status_trainer():
    response = requests.get(url=f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200