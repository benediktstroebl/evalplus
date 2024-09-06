def eat(n, need, rem):
    ate = n
    if ate + need > rem:
        (ate) = rem
    print(f'Result: [{ate}, {rem}]')
    return [ate, rem]