def eat(n, need, rem):
    ate = n
    if ate + need > rem:
        (ate) = rem
    print(f'rabbit eats {ate} carrots')
    print(f'because it needs to eat {need} carrots')
    print(f'but only {rem} carrots are left')
    return [ate, rem]