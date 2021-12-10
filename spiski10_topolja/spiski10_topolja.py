print('Добро пожаловать!')
tekst=input('Введи текст для редактирования - ')
answ=0
n=0
list_1 = list(tekst.strip(" "))
while 1:
    print('Что хотите сделать с текстом?')
    print('добавить элемент в конец текста (1)')
    print('дублировать текст (2)')
    print('добавить внутрь текста элемент (3)')
    print('удалить один определённый элемент (4)')
    print('переместить один определённый элемент (5)')
    print('сделать все буквы большими или маленькими (6)')
    print('узнать количество символов в тексте (7)')
    print('сортировать текст в правильном или обратном направлении (8)')
    print('перевернуть текст (9)')
    print('запятая после каждой буквы (10)')
    while type(answ)!=int or answ>10 or answ<=0:
        try:
            answ=int(input('Введите вариант ответа 1-10: '))
        except ValueError:
            print('Не верный вариант ответа!')
    if answ==1:
        letter=input('Какой элемент добавить в конец текста?: ')
        list_1.append(letter)
        print('Текст изменён на -',''.join(list_1))
    if answ==2:
        list_1.extend(list_1)
        print('Текст изменён на -',''.join(list_1))
    if answ==3:
        letter=input('Какой элемент добавить в конец текста?: ')
        place=int(input('После какого по счёту элемента вставить выбранный элемент?: '))
        place=place+1
        list_1.insert(place, letter)
        print('Текст изменён на -',''.join(list_1))
    if answ==4:
        letter=input('Какой элемент хотите удалить?: ')
        list_1.remove(letter)
        print('Текст изменён на -',''.join(list_1))
    if answ==5:
        letter=input('Какой элемент хотите выбрать?: ')
        place=int(input('После какого по счёту элемента вставить выбранный элемент?: '))
        place=place+1
        list_1.remove(letter)
        print('Текст изменён на -',''.join(list_1))
    if answ==6:
        BorS=int(input('Сделать большими(1) или маленькими(0)'))
        if BorS==1:
            print('Текст изменён на -',''.join(list_1).upper())
        if BorS==0:
            print('Текст изменён на -',''.join(list_1).lower())
        list_1 = list(tekst.strip(" "))
    if answ==7:
        nSimvolov=len(list_1)
        print(f'В тексте - {nSimvolov} символа')
    if answ==8:
        PRAVElorOBRAT=int(input('В правильном направлении(1) или в обратном направлении(0)'))
        if PRAVElorOBRAT==1:
            list_1.sort()
        if PRAVElorOBRAT==0:
            list_1.sort(reverse=True)
        print('Текст изменён на -',''.join(list_1))
    if answ==9:
        list_1.reverse()
        print('Текст изменён на -',''.join(list_1))
    if answ==10:
        print('Текст изменён на -',', '.join(list_1))
    answ=0
    cont=int(input('Хотите продолжить редактирование? Да(1), Нет(0): '))
    print()
    if cont==0:
        break
print('Спасибо за использования программы "SuperTextEditor"')
