
a = int(input('Введите лет: '))
pol =  str(input('Введите пол: '))
b = int(input('Введите отжимания: '))

if a in range(0,9):
    i = "6-8"
elif a in range(9,12):
    i = "9-11"
elif a in range(12,15):
    i = "12-14"
elif a in range(15,18):
    i = "15-18"
elif a in range(18,99):
    i = "18+"

print(i)

push_ups = { '6-8': { 'man': {1:5, 2:4, 3:3, 4:2, 5:'none'}, 'fam': { '14+':5, '13-10':4, '9-8':3, '8-3':2 } }, 
             '9-11':{ 'man': {'22-19':5, '18-15':4, '14-8':3, '7-0':2}, 'fam': { '14-11':5, '10-9':4, '8-4':3, '3-0':2 } } }

new_dict = push_ups.get(i)

if pol == "man":
    new_new_dict = new_dict.get('man')
    if b in range(22,1000):
        ii = 1
        print(new_new_dict.get(ii))
    elif b in range(18,22):
        ii = 2
        print(new_new_dict.get(ii))
    elif b in range(14,18):
        ii = 3
        print(new_new_dict.get(ii))
    elif b in range(7,14):
        ii = 4
        print(new_new_dict.get(ii))
    elif b in range(0,7):
        ii = 5
        print(new_new_dict.get(ii))
else:
    new_new_dict = new_dict.get('fam')


# print(new_new_dict)
