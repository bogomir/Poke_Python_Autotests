import requests
from faker import Faker
import random

TOKEN = 'a9661c322344a9d700781e713e7c2b21'
HOST = 'https://pokemonbattle.me:9104'

# Создаем покемона
answer_create_pokemon = requests.post(f'{HOST}/pokemons', json = {
                                          'name' : 'Пикачу',
                                          'photo' : 'https://dolnikov.ru/pokemons/albums/025.png'
                                      }, headers = {
                                          'Content-Type' : 'application/json',
                                          'trainer_token' : TOKEN
                                      })
print(answer_create_pokemon.json())

# Забираем id_pokemon из ответа
id_pokemon = answer_create_pokemon.json()['id']

# Переименовываем и меняем фото
fake = Faker()
answer_change_name = requests.put(f'{HOST}/pokemons', json = {
    'pokemon_id' : id_pokemon,
    'name' : fake.name(), 
    'photo' : f'https://dolnikov.ru/pokemons/albums/{random.randint(1,999):03}.png'
}, headers = {
    'Content-Type' : 'application/json',
    'trainer_token' : TOKEN
})

print(answer_change_name.json())

# Добавляем покемона в покеболл
answer_in_pokeball = requests.post(f'{HOST}/trainers/add_pokeball', json = {
    'pokemon_id' : id_pokemon
}, headers = {
    'Content-Type' : 'application/json',
    'trainer_token' : TOKEN
})

print(answer_in_pokeball.json())