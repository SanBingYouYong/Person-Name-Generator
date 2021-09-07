# with open("family_names.txt",'r', encoding='utf8') as file:
#     lines = file.readlines()
#     print(type(lines))
#     # print(lines[:100])
#     names = []
#     for line in lines:
#         name = line[:-1]
#         if name != "\t":
#             names.append(name)
#         # print(type(line))
#     # print(names)

# with open("family_names_clear.txt", 'w', encoding='utf8') as f:
#     for name in names:
#         f.writelines(str(name) + "\n")
with open("family_names_clear.txt", 'r', encoding='utf8') as f:
    family_names = []
    names = f.readlines()
    # print(type(names))
    for name in names:
        family_names.append(name[:-1])
    print(family_names)