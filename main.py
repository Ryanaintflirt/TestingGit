import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
data = response.json()

code = response.status_code()

print("Status code : ", code)
print("Name:", data['name'])
print("Height:", data['height'])
print("Weight:", data['weight'])
print("Abilities:", [a['ability']['name'] for a in data['abilities']])
