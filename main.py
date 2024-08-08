import requests

base_url = "https://catfact.ninja"


endpoint = '/breeds'
query_params = {'limit':3, 'page':4 }

response = requests.get(base_url+endpoint, params=query_params)
print(response.status_code)
print(response.text)


endpoint = '/fact'
query_params = {'max_length':30}

response = requests.get(base_url+endpoint, params=query_params)
print(response.status_code)
print(response.text)


endpoint = '/facts'
query_params = {'max_length': 60, 'limit': 5}

response = requests.get(base_url+endpoint, params=query_params)
print(response.status_code)
print(response.text)