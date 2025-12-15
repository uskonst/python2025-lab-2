# f = open("Coffee_sales.csv")

# f.close

import csv
import statistics

def rline(reader):
    fields = next(reader)
    print(" | ".join(fields))
    return fields

def slice(coffee, start, end):
    coffee.seek(0)
    r = csv.reader(coffee)
    for i in range(end):
        if i >= start:
            rline(r)
        else:
            next(r)
    
def findpop(coffee):
    coffee.seek(0)
    r = csv.DictReader(coffee)
    
    # res = statisrics.mode("")
    
    drinks = []
    for i in r:
        drinks.append(i["coffee_name"])
    # print(drinks)
    count = {d:0 for d in drinks}
    
    for d in drinks:
        count[d] += 1
    print(max(count, key=lambda k: count[k]))
        
# def month(coffee):
#     months = input("1-12 ")
#     coffee.seek(0)
#     r = csv.DictReader(coffee)
#     c = 0
#     for i in r:
#         if i["Monthsort"] == str(months):
#             c += float(i["money"])
#     print(c)
#     return c

if __name__ == "__main__":
    with open("Coffe_sales.csv") as coffee: # Лучше использовать этот метод открытия файла
        # slice(coffee, 8, 15)
        findpop(coffee)
        # month(coffee)
        
        
    