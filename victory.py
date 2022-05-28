def victory():

    correct_count = 0
    incorrect_count = 0

    Ford = input('В каком году родился Харрисон Форд? ')         #Харрисон Форд родился в 1942 году
    if Ford == '1942':
        correct_count += 1
    else:
        incorrect_count += 1

    Hauer = input('В каком году родился Рутгер Хауэр? ')        #Рутгер Хауэр родился в 1944 году
    if Hauer == '1944':
        correct_count += 1
    else:
        incorrect_count += 1

    Young = input('В каком году родилась Шо Янг? ')             #Шо Янг родилась в 1959 году
    if Young == '1959':
        correct_count += 1
    else:
        incorrect_count += 1

    Hannah = input('В каком году родилась Дэрил Ханна? ')       #Дэрил Ханна родилась в 1960 году
    if Hannah == '1960':
        correct_count += 1
    else:
        incorrect_count += 1

    James = input('В каком году родился Брайон Говард Джеймс? ')        #Брайон Говард Джеймс родился в 1945 году
    if James == '1945':
        correct_count += 1
    else:
        incorrect_count += 1

    print('Правильных ответов: ', correct_count)
    print('Неправильных ответов: ', incorrect_count)
    print('Процент правильных ответов: ', correct_count * 100 / 5)
    print('Процент неправильных ответов: ', incorrect_count * 100 / 5)

victory()
while True:
    play_again = input('Хотите сыграть еще раз? [да/нет]: ')

    if play_again == 'да':
        victory()
    else:
        break