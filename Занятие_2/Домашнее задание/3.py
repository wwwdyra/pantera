m=int(input('Введите номер месяца: '))
month=['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
if 1<=m<=12:
    print('Месяц -',month[m-1],'Время года - ', end='')
    if m==12 or 1<=m<=2:
        print('Зима')
    elif 3<=m<=5:
        print('Весна')
    elif 3<=m<=5:
        print('Лето')
    else:
        print('Осень') 
else:
    print('Недопустимое число!')