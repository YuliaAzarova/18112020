print('Введите неотрицательное меньше 100 число')
a = int(input())
if a > 95 or a == 95:
    print('5')
else:
    if a == 75 or a > 75 and a < 95:
        print('4')
    else:
        if a == 50 or a > 50 and a < 75:
            print('3')
        else:
            print('2')