

import requests
import json

# task 2
response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
json_data = response.text

pikachu_data = json.loads(json_data)

print(f"Pokemon name: {pikachu_data['name']}")
print(f"Pokemon abilities:  {pikachu_data['abilities']}")

# task 3
def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"  
    try:
        response = requests.get(url)
        json_data = response.text

        pokemon_data = json.loads(json_data)
        print(f"Pokemon name: {pokemon_data['name']}")
        print(f"Pokemon abilities:  {pokemon_data['abilities']}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

fetch_pokemon_data("charizard")
fetch_pokemon_data("bulbasaur")
fetch_pokemon_data("jigglypuff")


def calculate_average_weight(pokemon_list):
    pokemon_list = ["pikachu", "bulbasaur", "charmander"]
    total_weight = 0
    num_pokemon = len(pokemon_list)

    for pokemon in pokemon_list:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
        json_data = response.text
        pokemon_data = json.loads(json_data)
        total_weight += pokemon_data['weight']
    
    average_weight = total_weight / num_pokemon
    print(f"The three chosen pokemon are: {pokemon_list}")
    print(f"The average weight of the pokemon is: {average_weight}")


calculate_average_weight('pokemon_list')
