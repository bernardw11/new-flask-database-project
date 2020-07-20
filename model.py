import requests

def getPokemonData(poke_choice):
    pokemon_query = f"https://pokeapi.co/api/v2/pokemon/{poke_choice}"
    poke_data = requests.get(pokemon_query).json()
    data_dict = {}
    data_dict['name'] = poke_choice
    data_dict['ability'] = poke_data['abilities'][0]['ability']['name']
    data_dict['hp'] = poke_data['stats'][0]['base_stat']
    data_dict['att'] = poke_data['stats'][1]['base_stat']
    data_dict['def'] = poke_data['stats'][2]['base_stat']
    data_dict['spatt'] = poke_data['stats'][3]['base_stat']
    data_dict['spdef'] = poke_data['stats'][4]['base_stat']
    data_dict['spd'] = poke_data['stats'][5]['base_stat']
    return data_dict
