import os
import pprint


def create_data():
    string = []

    file = os.path.abspath('personas.txt')
    with open (file, 'r') as f:
        string = [l.strip(' \n') for l in f.readlines()]

    list_personas = [string[i-2:i+1] for i, line in enumerate(string) if line.startswith('Eager')]

    dict_personas = []
    for j, k in enumerate(list_personas):
        #dict_personas[j] = {}
        dict_personas.append({'persona': k[0]})
        for item in k[1:]:
            key, value = item.split(': ')
            dict_personas[j][key] = value.split(', ')

    return dict_personas


def main(data):
    persona = input('Введи название персоны:\n')
    for item in data:
        if item['persona'] == persona:
            print('Eager:', *item['Eager'], '\nHappy:', *item['Happy'])


if __name__ == '__main__':
    data = create_data()
    main(data)
