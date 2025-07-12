import requests



def test_pokemon_endpoint():
    assert requests.get("https://pokeapi.co/api/v2/pokemon", timeout=5).status_code == 200
