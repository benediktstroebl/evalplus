def eat(n, need, rem):
    ate = n
    if need > rem:
        ate = rem
    else:
        ate += need
    return [ate, rem - ate]