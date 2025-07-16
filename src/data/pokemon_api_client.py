import json
import time
import logging
import requests


OFFSET = 0
LIMIT = 50
POKEMON_DATA_URL = f'https://pokeapi.co/api/v2/pokemon?offset={OFFSET}&limit={LIMIT}'
DATA_LOCATION = 'raw_pokemon_pages'
TIMEOUT_SEC = 5
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Requesting data on url: %s", POKEMON_DATA_URL)
response = requests.get(POKEMON_DATA_URL, timeout=TIMEOUT_SEC)


# First request
if response.status_code == 200:
    logging.info("Request successful")
    # First page
    page = 1            # This is not a constant pylint: disable=C0103
    json_data = response.json()
    logging.debug("Data: %s", json_data)
    with open(f"{DATA_LOCATION}/pokemon_{page}.json", mode='w', encoding='utf-8') as file:
        json.dump(json_data["results"], file, indent=4)

next_page = json_data["next"]


while next_page is not None:
    # Keeps from overloading the API
    time.sleep(3)
    # Next json page
    page += 1
    response = requests.get(next_page, timeout=TIMEOUT_SEC)
    json_data = response.json()
    logging.debug("Data %s", json_data)
    with open(f"{DATA_LOCATION}/pokemon_{page}.json", mode='w', encoding='utf-8') as file:
        json.dump(json_data["results"], file, indent=4)

    # Set next page url
    next_page = json_data["next"]
