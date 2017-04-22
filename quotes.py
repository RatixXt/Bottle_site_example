from json import loads
from codecs import open
from random import choice


def load_json(path_to_json='quotes.json'):
    with open(path_to_json, 'r', 'utf-8') as json_data:
        return loads(json_data.read())


def choose_quote():
    data = load_json()
    return choice(data)


def choose_quote_by_id(id):
    data = load_json()
    if len(data) <= id:
        return None
    return data[id]


# небольшой тест
if __name__ == '__main__':
    dict_quote = choose_quote()
    print(dict_quote['id'], dict_quote['phrase'], dict_quote['signature'])
    print(choose_quote_by_id(1))
