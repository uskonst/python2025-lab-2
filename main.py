import csv
import random
import xml.etree.ElementTree as ET

AUTHOR_KEY = 'Автор'
DATE_KEY = 'Дата поступления'
TITLE_KEY = 'Название'

def get_year(date):
    return int(date.split('.')[-1].split()[0])

with open('books.csv', encoding='cp1251') as file:
    rows = list(csv.DictReader(file, delimiter=';'))

# Задание 1
count = sum(len(row[TITLE_KEY]) > 30 for row in rows)
print('Задание 1:', count)

# Задание 2
author = input("Автор:")
filtered_books = []
for row in rows:
    year = get_year(row[DATE_KEY])      
    if author in row[AUTHOR_KEY] and year in {2014, 2016, 2017}:
        filtered_books.append(row)

print('Задание 2:')
for book in filtered_books:
    print(book[AUTHOR_KEY], book[TITLE_KEY], get_year(book[DATE_KEY]))

# Задание 3
bibliography = random.sample(rows, 20)

with open('bibliography.txt', 'w', encoding='utf-8') as file:
    for index, book in enumerate(bibliography, start=1):
        file.write(f"{index}. {book[AUTHOR_KEY]}. {book[TITLE_KEY]} - {get_year(book[DATE_KEY])}\n")
print('Задание 3: Файл завершен')

# Задание 4
tree = ET.parse('currency.xml')
root = tree.getroot()

print('Задание 4:')
for valute in root.findall('Valute'):
    Nominal = valute.find('Nominal').text
    if Nominal == 1:
        Name = valute.find('Name').text
        print(Name)