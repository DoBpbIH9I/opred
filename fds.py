import json
import os
import time
from pprint import pprint

def parse_recipes():
    """Возвращает словарь с рецептами
    берущихся из файла перечня recipes.txt"""
    with open("recipes.txt", encoding="utf-8") as file:
        cook_book = {}
        for line in file.read().split("\n\n"):
            meal_name, *ingredients = line.split("\n")
            cook_lst = []
            for ingredient in ingredients[1:]:
                ingredient_name, quantity, measure = ingredient.split(" | ")
                cook_lst.append(
                    {
                        "ingredient_name": ingredient_name,
                        "quantity": int(quantity),
                        "measure": measure,
                    }
                )
            cook_book[meal_name] = cook_lst
        del cook_book["Фахитос"]
    return cook_book
cook_book = parse_recipes()

# print(parse_recipes())

def get_shop_list_by_dishes(dishes, person_count):
    """Создает список покупок для блюд по количеству
    персон из перечня рецептов"""
    new_cook = {}
    for dish in dishes:
        for ingredient in parse_recipes()[dish]:
            new_cook2 = {}
            if ingredient["ingredient_name"] not in new_cook:
                new_cook2['measure'] = ingredient['measure']
                new_cook2['quantity'] = ingredient['quantity'] * person_count
                new_cook[ingredient['ingredient_name']] = new_cook2
            else:
                new_cook[ingredient['ingredient_name']]['quantity'] = \
                    new_cook[ingredient['ingredient_name']]['quantity'] + ingredient['quantity'] * person_count

    return new_cook

pprint(get_shop_list_by_dishes(["Омлет", "Утка по-пекински"], 9))

def strings_count(file):
    with open(file, 'r', encoding= 'utf-8') as f:
        return sum(1 for line in f)

base_path = os.getcwd()
location = os.path.abspath('sorted')
file_for_write = os.path.abspath('sorted/rewrite_file.txt')
full_path = os.path.join(base_path, location)
def rewrite(full_path, file_for_write):
    files = []
    for i in list(os.listdir(full_path)):
        files.append([strings_count(os.path.join(full_path, i)), os.path.join(base_path, location, i), i])
    for file_item in sorted(files):
        opening_files = open(file_for_write, 'a', encoding= 'utf-8')
        opening_files.write(f'{file_item[2]}\n')
        opening_files.write(f'{file_item[0]}\n')
        with open(file_item[1], 'r', encoding= 'utf-8') as file:
            counting = 1
            for line in file:
                opening_files.write(f'строка № {counting} в файле {file_item[2]} : {line}')
                counting += 1
        opening_files.write(f'\n')
        opening_files.close()
rewrite(full_path, file_for_write)

pprint(get_shop_list_by_dishes(['Омлет', 'Омлет'], 2))
pprint(get_shop_list_by_dishes(['Утка по-пекински', 'Утка по-пекински'], 2))
