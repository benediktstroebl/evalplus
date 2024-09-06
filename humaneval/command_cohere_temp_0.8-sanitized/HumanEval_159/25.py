def eat(n, need, rem):
    dist = need - n
    if dist > rem:
        dist = rem
    n += dist
    rem -= dist
    return [n, rem]