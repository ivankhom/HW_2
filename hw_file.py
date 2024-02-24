from pprint import pprint


def create_cook_book(file_path):
    cook_book = {}

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]

        while lines:
            dish_name = lines.pop(0)
            ingredient_count = int(lines.pop(0))
            ingredients = []

            for _ in range(ingredient_count):
                ingredient_data = lines.pop(0).split(' | ')
                ingredient_name = ingredient_data[0]
                quantity = int(ingredient_data[1])
                measure = ingredient_data[2]
                ingredient_info = {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure}
                ingredients.append(ingredient_info)

            cook_book[dish_name] = ingredients

    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in cook_book:
        ingredients = cook_book[dish]
        for ingredient in ingredients:
            name = ingredient['ingredient_name']
            measure = ingredient['measure']
            quantity = ingredient['quantity'] * person_count
            if name in shop_list:
                shop_list[name]['quantity'] += quantity
            else:
                shop_list[name] = {'measure': measure, 'quantity': quantity}

        return shop_list


cook_book = create_cook_book('recipes(1).txt')
pprint(cook_book)
pprint(get_shop_list_by_dishes(['Омлет'], 2))
