import requests
import json

#  POST add new pet

base_url="https://petstore.swagger.io/v2"
post_url = '/pet'
headers_post = {'accept': 'application/json', 'Content-Type': 'application/json'}
new_pet = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "predator"
  },
  "name": "Monster",
  "photoUrls": [
    "mon_foto"
  ],
  "tags": [
    {
      "id": 0,
      "name": "danger"
    }
  ],
  "status": "pending"
}
data_post = json.dumps(new_pet)

res = requests.post(base_url + post_url, headers=headers_post, data=data_post)

print(res.status_code)
print(res.json())
x=res.json()
# print(x["id"])


# GET find pet by ID

url = "https://petstore.swagger.io/v2/pet/"
id = str(x["id"])

res = requests.get(url + id, headers={'accept': 'application/json'})

print(res.status_code)
print(res.json())

# PUT update an existing pet

base_url="https://petstore.swagger.io/v2"
post_url = '/pet'
headers_put = {'accept': 'application/json', 'Content-Type': 'application/json'}
new_name = {'id': id, 'category': {'id': -15301108, 'name': 'Ut enim occaecat aute'},
            'name': 'New_doggie', 'photoUrls': ['elit ad', 'pariatur elit'],
            'tags': [{'id': 62572940, 'name': 'exercitation in elit ut ea'},
            {'id': -25174988, 'name': 'ut amet aliquip'}], 'status': 'pending'}
data_put = json.dumps(new_name)

res = requests.put(base_url + post_url, headers=headers_put, data=data_put)
print(res.status_code)
print(res.json())

# DELETE delete a pet

url = "https://petstore.swagger.io/v2/pet/"
# id = id

res = requests.delete(url + id, headers={"accept": "application/json", "api_key": "special-key"})

print(res.status_code)
print(res.json())








