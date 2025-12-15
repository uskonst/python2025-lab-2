import csv, random
# import xml.etree.ElementTree as ET

# csv read
with open('books.csv', encoding='cp1251') as f:
    rows = list(csv.DictReader(f, delimiter=';'))

# keys
title_key = 'Название'
author_key = 'Автор'
date_key = 'Дата поступления'

# task1
count = sum(len(r[title_key]) > 30 for r in rows)
print("ans1:", count)

# task2
author = input("author?:")
filtered = []
for r in rows:
    try:
        year = int(r[date_key].split('.')[-1].split()[0])
        # print(int(r[date_key]))
        print(int(r[date_key].split('.')[-1]))
        if author in r[author_key] and 2016 <= year <= 2018:
            filtered.append(r)
    except:
        pass

print('ans2:', len(filtered))
for r in filtered[:3]:
    print(r[author_key], r[title_key], r[date_key])


# # task3
# bibs = random.sample(rows, 20)
# with open('bibliography.txt', 'w', encoding='utf-8') as f:
#     for i, b in enumerate(bibs, 1):
#         f.write(f"{i}. {b[author_key]}. {b[title_key]} - {b[date_key]}\n")
# print('file done')
# input("press enter")

# # xml
# tree = ET.parse('currency.xml')
# root = tree.getroot()
# for val in root.findall('.//Valute'):
#     if int(val.find('Nominal').text) in (10, 100):
#         print(val.find('CharCode').text)