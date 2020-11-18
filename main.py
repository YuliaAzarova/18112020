print('Ориентир градин')
a = int(input())
print('Введите количество градин больше чем в 1 раз')
b = int(input())
print('Введите количество градин')
f = int(input())
if f < a:
    print('NO GRAD')
else:
    if f > a and f < b:
        print('GRAD')
    else:
        print('grad')