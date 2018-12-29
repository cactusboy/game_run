import sys

file = open("readme.md", "r", encoding='UTF-8')
all_data = file.readlines()
print(all_data)
file.close()