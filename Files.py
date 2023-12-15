# -*- coding: utf-8 -*-

from dataclasses import fields
import pandas as pd # Интерфейс под читалки экселя
import json # Работа с джисоном

# Вывод содержимого файла построчно
def print_file(filename):
    with open(filename, 'r') as file: # способ открывать файл немножко проще
        for line in file:
            print(line.strip()) # без strip() в консоли между строками много пустоты


filename = 'file.txt'   #имя файла
joe_b = 'text_with_joe_biden.txt'
json_stethem = 'data.json'

# Создание текстового файла
with open(filename, 'w') as file:
    for i in range(1, 100+1):
        file.write(f"Строка: {i}\n")


print_file(filename)

# Замена каждой 3-й строки
with open(filename, 'r') as file:
    lines = file.readlines()

for i in range(1, 99, 3):
    lines[i] = "Joe Biden\n"

# Запись изменений в файл
with open(joe_b, 'w') as file:
    file.writelines(lines)


print_file(joe_b)



# Чтение Excel файла и поиск минимума и максимума
df_read = pd.read_excel('C:/Users/kiril/OneDrive/Рабочий стол/Проекты на путоне/Files/data.xlsx', index_col=0)

for column in df_read.columns:
    min_value = df_read[column].min()  # минимум
    max_value = df_read[column].max()  # максимум
    print(f"Минимум = {min_value}, Максимум = {max_value}")
    

# Чтение из текстового файла
with open('file.txt', 'r') as file:
    lines = [line.strip() for line in file]

# Создание JSON (Стетхем)
jd = {'lines': lines}

with open(json_stethem, 'w') as json_file:
    json.dump(jd, json_file)

with open(json_stethem, 'r') as json_file:
    fields = json.load(json_file)
    
print(fields)