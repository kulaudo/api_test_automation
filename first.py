import requests

url = "https://reqres.in/api/users?page=2"

response = requests.get(url)

list_i = response.json()['data']
print(len(list_i))


