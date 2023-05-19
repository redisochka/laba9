from PIL import Image, ImageFilter
import os
import csv

def xd1():

    if not os.path.exists('new'):
        os.mkdir('new')

    filter_type = ImageFilter.EMBOSS
    source_folder = "C:/Users/HP/Desktop/xd/Учеба/Программирование/9_лаба/old"
    for filename in os.listdir(source_folder):
        image = Image.open(os.path.join(source_folder, filename))
        filtered_image = image.filter(filter_type)
        filtered_image.save(os.path.join('new', 'processed_' + filename))

def xd2():

    if not os.path.exists('new'):
        os.mkdir('new')

    filter_type = ImageFilter.EMBOSS
    source_folder = "C:/Users/HP/Desktop/xd/Учеба/Программирование/9_лаба/old"
    for filename in os.listdir(source_folder):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            image = Image.open(os.path.join(source_folder, filename))
            filtered_image = image.filter(filter_type)
            filtered_image.save(os.path.join('new', 'processed_' + filename))

def xd3():

    total_cost = 0
    with open('Продукты.csv') as r_file:
        reader = csv.reader(r_file, delimiter=",")
        next(reader)
        print("Нужно купить: ")
        for row in reader:
            product = row[0]
            quantity = row[1]
            price = row[2]
            cost = int(quantity) * int(price)
            total_cost += cost
            print(f"{product} - {quantity} шт. за {price} руб.")
    print(f"Итоговая сумма: {total_cost} руб.")

xd1()
xd2()
xd3()
