def eat(n, need, rem):
    temp = n + need
    if temp > rem:
        temp = rem
    print(f'Rabbit eats {need} carrots')
    print(f'Carrots remaining: {rem-temp}')
    return [temp, rem-temp]