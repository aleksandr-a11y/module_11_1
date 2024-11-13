from PIL import Image, ImageOps # модуль оброботки изображения


with Image.open("123.jpg") as im:
    im.rotate(45).show() #поворачивает картинку на 45 градусов


size = (100, 150)
with Image.open("123.jpg") as im:
    ImageOps.contain(im, size).save("imageops_contain.webp") #делает картинку маленькой
    ImageOps.invert(im).save("321.jpg") # инвертирует картинку и сохроняет в файл

import requests

# Запрос данных с сайта
response = requests.get('https://api.github.com')
# Вывод ответа в консоль
print(response.json())  # Печатает JSON-ответ от GitHub API
print("\n код requests завершён \n")

import numpy as np
#Создаем массив с помощью библиотеки numpu

arr = np.array([10, 20, 30, 40, 50])
result = arr + 10
print("Массив увеличенный на 10:", result)
print(f'Минимальное значение массива: {result.min()}')
print(f'Максимальное значение массива: {result.max()}')
print(f'Сумма всех элементов массива: {result.sum()}')