import json
import openai

# EXTRACT - pegar o nome dos jogos para a pesquisa

file = open("games_data.json")
data = json.load(file)


names = []
for k, v in data.items():
    names.append(v["game"])


# TRANSFORM

openai.api_key = "sua api key"


def get_game_info(game):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You're a gaming industry specialist."},
            {"role": "user", "content": f"Give release date, platform and metacritic rating for {game}."},
        ]
    )
    return response['choices'][0]['message']['content']


for i, game in enumerate(names):
    info = get_game_info(game)
    if data[f"{i}"]["info"] == []:
        data[f"{i}"]["info"].append(info)


# LOAD


data = json.dumps(data, indent=4)

with open("games_data.json", "w") as file:
    file.write(data)
