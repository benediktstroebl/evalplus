def eat(n, need, rem):
    if need > rem:
        eat_all = rem
        hunger = need - rem
    else:
        eat_all = need
        hunger = 0
    return [n + eat_all, hunger]