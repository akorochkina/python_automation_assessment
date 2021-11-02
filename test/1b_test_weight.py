import requests

def get_url(url):
    x = requests.get(url)
    #print(x.json())
    return x.json()

def get_truck_weight(data):
    return data["planned_route"]["resource"]["carrying_capacity"]

def get_deliveries_weight(data):
    deliveries_list = data["planned_route"]["deliveries"]
    weight_of_deliveries = 0
    for item in deliveries_list:
        if 'algorithm_fields' in item:
            if 'weight' in item["algorithm_fields"]:
                weight_of_deliveries = weight_of_deliveries + item["algorithm_fields"]["weight"]
    return weight_of_deliveries

def test_weight():
    json_response = get_url('https://my-json-server.typicode.com/akorochkina/mock2/db')
    truck_weight = get_truck_weight(json_response)
    deliveries_weight = get_deliveries_weight(json_response)
    assert truck_weight > deliveries_weight
