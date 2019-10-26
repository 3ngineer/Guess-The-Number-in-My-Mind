import random
first = 1
second = 99
count_hads = 0

hads = random.randint(first, second)
print('hads= ', hads)
javab = input('user idea(b-k-d): ')
while javab != 'd':
    if javab == 'b':
        first = hads
        hads = random.randint(first, second)
        print('hads: ', hads)

    else:
        second = hads
        hads = random.randint(first, second)
        print('hads: ', hads)
    javab = input('user idea(b-k-d): ')

print('wooooow!!! you did it, u r a genius')

