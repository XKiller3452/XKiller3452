import datetime
from threading import Timer
from time import sleep

holodos = {}


pool = {}
any = []
ary = []

df = []
dg = []

# Основное меню




def gammy():
    alert()
    global any
    global ary
    global holodos



    print("1) Список")
    print("2) Холодос")
    q = input("Ввод: ")



    # Меню Списка покупок


    if q == "1" or q == "Список":
        print("1) Добавить продукты в список")
        print("2) Показать список")
        print("3) Очистить список")
        print("4) Назад")
        k = input("Ввод: ")
        if k == "1":
            spis()

        elif k == "2":
            if pool == {}:
                print('Список пуст')
            else:
                print(pool)

        elif k == "3":
            pool.clear()
            print("Список пуст")
        elif k == "4":
            alert()
            gammy()
        else:
            print("Ввод не верный! ")


    elif q == "Холодос" or q == "2":
        mon()
    gammy()



    # Меню Холодоса


def mon ():
    alert()

    # Основное меню

    global holodos
    global any
    global ary
    print("1) Очистить Холодильник")
    print("2) Открыть Холодильник")
    print('3) Удалить позицию ')
    print('4) Назад')
    op = input("Ввод: ")
    if op == "2":
        if holodos != {}:           # Проверка,есть что-то  холодосе или нет
            print(holodos)
        else:
            add_hol()

        print('1) Назад')
        print('2) Добавить продукты')
        a = input("Что хотим?: ")
        if a == '1':
            mon()
        elif a == '2':
            add_hol()

    elif op == "1":
        holodos.clear()
        print("Холодос пуст")
    elif op == '4':
        gammy()
    elif op == ' ' or op == '':
        pass
    elif op == '3':
        dell_key()
    else:
        print("Не верный ввод! ")


        #Ниже функция для добавления продуктов в холодос




def add_hol():

    global holodos
    global ary
    global any
    e = input("Что и сколько будем класть в Холодильник? (Beta): ")
    if e == '' or e == ' ':
        print('Неверный ввод')
    elif e != '' or e != ' ':
        for i in e:
                                                   # Проверка, есть ли в переменной g буквы
                                                   # если да,то происходит сортировка по спискам,
                                                   # буквы присваиваются переменной any, а цифры в переменную ary


            if i.isdigit() == True:
                ary.append(i)
            elif i.isdigit() == False:
                any.append(i)
        else:
            pass
        any = ''.join(any)
        ary = ''.join(ary)
        any = any.replace(" ", '')
        ary = ary.replace(' ', '')
        if any == [] or any == '' or ary == [] or ary == '':
            print('Неверный ввод')
            any = list(any)
            ary = list(ary)
            any.clear()
            ary.clear()
        else:
            holodos[any] = ary
            any=list(any)
            ary=list(ary)


            any.clear()
            ary.clear()
        print(holodos)






    # Функция добавления продуктов в список

def spis():
    alert()
    u = input("Добавить продукт: ")
    j = input("Количество: ")
    if j == '' or j == " ":
        print("Неверный ввод")
    elif u == '' or u == " ":
        print('Неверный ввод')
    else:
        u = u.replace(' ', '')
        j = j.replace(' ', '')
        pool[u] = j
        print(pool)




        # Удаление по ключу


def dell_key():
    alert()
    print(holodos)
    g = input('Что удалить?: ')
    if g == '' or g == ' ':
        print("Неверный ввод")
    elif holodos[g] == None:
        print('Тут такого нет')
    else:
        del holodos[g]
        print('Позиция удалена')


    # Проверяет количество продуктов в холодосе

def alert():
    for i in holodos.keys():
        if holodos.get(i) <= '2':
            print('У вас кончается ' + i + ',' + ' осталось ' + holodos.get(i) + ' шт.')
        else:
            pass








gammy()
mon()
add_hol()
spis()
dell_key()
alert()