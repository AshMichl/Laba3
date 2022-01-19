from random import randrange

class Box:
  def __init__ (self, item=None):
    self.item = item
    self.nextitem = None

class LinkedList:
  def __init__(self):
    self.head = None

  def contains (self, item):
    lastbox = self.head
    while (lastbox):
      if item == lastbox.item:
        return True
      else:
        lastbox = lastbox.nextitem
    return False

  def addToEnd(self, newitem):
    newbox = Box(newitem)
    if self.head is None:
      self.head = newbox
      return
    lastbox = self.head
    while (lastbox.nextitem):
        lastbox = lastbox.nextitem
    lastbox.nextitem = newbox


  def get(self, itemIndex):
    lastbox = self.head
    boxIndex = 0
    while boxIndex <= itemIndex:
      if boxIndex == itemIndex:
          return lastbox.item
      boxIndex = boxIndex + 1
      lastbox = lastbox.nextitem

  def removeBox(self,rmitem):
    headitem = self.head

    if headitem is not None:
      if headitem.item == rmitem:
        self.head = headitem.nextitem
        headitem = None
        return
    while headitem is not None:
      if headitem.item == rmitem:
        break
      lastitem = headitem
      headitem = headitem.nextitem
    if headitem == None:
      return
    lastitem.nextitem = headitem.nextitem
    headitem = None

  def len(self):
      current = self.head
      count = 0
      while current:
          count += 1
          current = current.nextitem
      return count


  def swap(self,itemindex):
    currentitem = self.head
    index = 0
    while index != self.len():
        if index == itemindex:
            self.addToEnd(currentitem.item)
            self.removeBox(currentitem.item)
        index += 1
        currentitem = currentitem.nextitem



  def LLprint(self):
    currentitem = self.head
    print("-----")
    i = 0
    while i != self.len():
      print (str(i) + ": " + str(currentitem.item))
      i += 1
      currentitem = currentitem.nextitem
    print("-----")

a = LinkedList()
print("Выберите действие")
print(" 1 - Сгенерировать\n", "2 - Добавить элемент списка\n", "3 - Обмен обмен элемнта с последним\n",
      "4 - Определить кразмер списка\n", "5 -Удалить элемнт\n", "6 -Вывести элемент\n",
      "7 - Вывести стек\n", "8 - Выход")
b = 1
while b !=0:
    x = int(input("Ваш выбор "))
    if x == 1:
        z = int(input("Введите размер "))
        for i in range (z):
          elem = randrange(1, 100)
          a.addToEnd(elem)
        a.LLprint()
    elif x == 2:
        z = int(input("Введите элемент "))
        a.addToEnd(z)
        a.LLprint()
    elif x == 3:
        z = int(input("Введите элемент "))
        a.swap(z)
        a.LLprint()
    elif x == 4:
        print("Количество элементов = ", a.len())
    elif x == 5:
        z = int(input("Введите элемент "))
        a.removeBox(z)
        a.LLprint()
    elif x == 6:
        z = int(input("Введите элемент "))
        print(a.get(z))
    elif x == 7:
        a.LLprint()
    elif x == 8:
        b=0





