import os, sys  # Несколько импортов в одной строке (ошибка стиля)

def my_function( name):  # Лишний пробел перед аргументом
    x=  10  # Неправильное форматирование
    if x > 5: print("X is greater than 5")  # Однострочная конструкция if (ошибка стиля)
    return  x+5 # Лишний пробел

my_function("World")
