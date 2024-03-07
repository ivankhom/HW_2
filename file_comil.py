import os
file_list = os.listdir('files')
txt_list = []
grand_dict = {}
for files in file_list:
    if files.endswith('.txt'):
        txt_list.append(files)
for file in txt_list:
    with open(os.path.join('files', file), 'r', encoding='utf-8') as f:
        content = f.read()
        grand_dict[file] = len(content)
sorted_dict = dict(sorted(grand_dict.items(), key=lambda item: item[1]))
with open('compil.txt', 'w', encoding='utf-8') as compil_f:
    for key, value in sorted_dict.items():
        with open(os.path.join('files', key), 'r', encoding='utf-8') as f:
            content = f.read()
            compil_f.write(f"{key}\n{value}\n")
            compil_f.write(content)
            compil_f.write('\n\n')




