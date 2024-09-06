def eat(n, need, rem):
    ct = n + need
    if ct > rem:
        ct = rem
    return [ct, rem-ct]