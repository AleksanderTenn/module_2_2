first= int(input('Введите первое число: '))
second=int(input('Введите второе число: '))
third= int(input('Введите третье число: '))
if first==second==third:
    print('Количество совпадений:',3)
elif first==second or first==third or second==third:
    print('Количество совпадений:',2)
else:
    print('Количество совпадений:',0)
