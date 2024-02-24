file_list = ['1.txt', '2.txt', '3.txt']
a_list = []


def line_count(file_name):
    count = 0
    with open(file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        return lines, file_name, len(lines)


for file in file_list:
    a = line_count(file)
    a_list.append(a)

with open('compil.txt', 'w', encoding='utf-8') as compil_f:
    for item in a_list:
        compil_f.write(f"{item[1]}\n{str(item[2])}\n")
        compil_f.writelines(item[0])


