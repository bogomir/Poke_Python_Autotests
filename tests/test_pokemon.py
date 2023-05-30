import requests
import pytest

TOKEN = 'a9661c322344a9d700781e713e7c2b21'
HOST = 'https://pokemonbattle.me:9104'

def test_status_code():
    answer_trainer_info = requests.get(f'{HOST}/trainers')
    assert answer_trainer_info.status_code == 200

def test_trainer_name():
    answer_trainer_name = requests.get(f'{HOST}/trainers', params = {'trainer_id' : '4264'})
    assert answer_trainer_name.json()['trainer_name'] == 'Иван'

@pytest.mark.parametrize('key, value', [('trainer_name', 'Иван'), 
                                        ('city', 'Иркутск'),
                                        ('level', '5')])

def test_trainer_name(key, value):
    answer_trainer_name = requests.get(f'{HOST}/trainers', params = {'trainer_id' : '4264'})
    assert answer_trainer_name.json()[key] == value
