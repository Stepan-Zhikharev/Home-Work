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
def rewrite(full_path, file_for_write):
    path = []
    files_for_writing = {}
    for name in list(os.listdir(full_path)):
        if name.endswith('.txt'):
            path.append(os.path.join(full_path, name))
    for file in path:
        with open(file, 'r', encoding='utf-8') as f:
            data = f.read()
            files_for_writing.update({os.path.basename(file): [str(len(data.split('\n'))), data]})
    files = dict(sorted(files_for_writing.items(), key=lambda x: x[1][0]))
    for write, file in files.items():
        with open(file_for_write, 'a', encoding='utf-8') as f:
            f.write(write)
            f.write('\n')
            f.write(file[0])
            f.write('\n')
            f.write(file[1])
            f.write('\n')