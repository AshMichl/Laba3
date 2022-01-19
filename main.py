from random import randrange

# n = int(input("Введите размер "))
n = randrange(1, 10)
def swap(Mas):
    temp = Mas[len(Mas) - 1]
    temp2 = Mas[len(Mas) - 2]
    Mas.remove(Mas[len(Mas) - 1])
    Mas.remove(Mas[len(Mas) - 2])
    Mas.insert(len(Mas), temp2)
    Mas.insert(len(Mas) - 1, temp)
    return Mas


mas = [randrange(1, 100) for i in range(n)]
print(mas)
print("Выберите действие")
print(" 1 - Поместить элемент на верх стека\n", "2 - Удалить верхушку стека\n", "3 - Обмен значений верхних элементов\n",
      "4 - Определить количество элементов в стеке\n", "5 - Очистка стека\n", "6 - Чтение верхнего элемнта\n",
      "7 - Вывести стек\n")
a = 1
while a !=0:
    x = int(input("Ваш выбор "))
    if x == 1:
        a = int(input("Введите элемент "))
        mas.append(a)
        print(mas)
    elif x == 2:
        mas.pop()
        print(mas)
    elif x == 3:
        swap(mas)
        print(mas)
    elif x == 4:
        print("Количество элементов = ", len(mas))
    elif x == 5:
        mas.clear()
        print(mas)
    elif x == 6:
        print(mas[len(mas) - 1])
        print(mas)
    elif x == 7:
        print(mas)
    elif x == 8:
        a=0
