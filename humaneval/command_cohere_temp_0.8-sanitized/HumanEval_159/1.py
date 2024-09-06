def eat(n, need, rem):
    temp = n + need
    if temp > rem:
        temp = rem
    n += temp
    return [n, rem-temp]