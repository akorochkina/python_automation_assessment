import requests

def get_url(url):
    x = requests.get(url)
    return x.json()

def get_planned_list_ids(url):
    response = get_url(url)
    list_planned = response["route"]
    list_planned_current_state_ids = list()
    for item in list_planned:
        if item["current_state"] == "planned":
            list_planned_current_state_ids.append(item["id"])
    return list_planned_current_state_ids

def get_deliveries_list_ids(url):
    response = get_url(url)
    list_all_deliveries = response["planned_route"]["deliveries"]
    list_all_deliveries_ids = list()
    for item in list_all_deliveries:
        list_all_deliveries_ids.append(item["id"])
    return list_all_deliveries_ids
    
def compare_lists(list1, list2):
    match_counter=0
    for item in list1:
        if item in list2:
            match_counter = match_counter+1
    if len(list1) == match_counter:
        return True
    else:
        return False

def test_planned_deliveries_are_included_into_all_deliveries():
    planned_deliveries = get_planned_list_ids('https://my-json-server.typicode.com/akorochkina/mock/db')
    all_deliveries = get_deliveries_list_ids('https://my-json-server.typicode.com/akorochkina/mock2/db')
    match = compare_lists(planned_deliveries, all_deliveries)
    assert match


