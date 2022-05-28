bornyear = input('В каком году родился А.С. Пушкин? ')

if bornyear == '1799':
    bornday = input('А в какой день? ')
    if bornday == '26.05':
        print('Верно!')
    else:
        print('Неверный день рождения!')

else:
    print('Неверный год рождения!')

