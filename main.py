import os
with open("recipes.txt", "r", encoding="utf-8") as f:
    data = f.read()
def cook_book_dict(recipes):
    cook_book = {}
    sp_list = data.split("\n\n")
    for i in sp_list:
        sp_dish = i.split("\n")
        for i in range(1, len(sp_dish)):
            value_out = sp_dish[i].split(" | ")
            value = {}
            value['ingredient_name'] = value_out[0]
            value['quantity'] = int(value_out[1])
            value['measure'] = value_out[2]
            if sp_dish[0] in cook_book:
                cook_book[sp_dish[0]].append(value)
            else:
                cook_book[sp_dish[0]] = [value]
    return cook_book
def get_shop_list_by_dishes(dishes, person_count):
    dish = {}
    for c in dishes:
        for x in cook_book_dict(data)[c]:
            if x['ingredient_name'] not in dish:
                dish[x['ingredient_name']] = {'measure' : x['measure'], 'quantity' : x['quantity'] * person_count}
            else:
                dish[x['ingredient_name']]['quantity'] += x['quantity'] * person_count

    return dish
def writing_file(first_file, second_file, third_file, result_file):
    with open(first_file, "r", encoding="utf-8") as f:
        first_string = f.read()
        first_list = first_string.split("\n")
        name_first_file = os.path.basename(first_file)
        number_first_file = str(len(first_list))
    with open(second_file, "r", encoding="utf-8") as f:
        second_string = f.read()
        second_list = second_string.split("\n")
        name_second_file = os.path.basename(second_file)
        number_second_file = str(len(second_list))
    with open(third_file, "r", encoding="utf-8") as f:
        third_string = f.read()
        third_list = third_string.split("\n")
        name_third_file = os.path.basename(third_file)
        number_third_file = str(len(third_list))
    with open(result_file, "w", encoding="utf-8") as f:
        f.write(name_second_file)
        f.write("\n")
        f.write(number_second_file)
        f.write("\n")
        f.write(second_string)
        f.write("\n")
        f.write(name_first_file)
        f.write("\n")
        f.write(number_first_file)
        f.write("\n")
        f.write(first_string)
        f.write("\n")
        f.write(name_third_file)
        f.write("\n")
        f.write(number_third_file)
        f.write("\n")
        f.write(third_string)