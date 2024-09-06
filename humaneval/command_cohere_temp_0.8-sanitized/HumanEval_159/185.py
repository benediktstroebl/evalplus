def eat(n, need, rem):
    ng, nm = 0, 0
    if n+need > rem:
        ng = n+need
        nm = rem
    else:
        ng = n+need
        nm = n
    return [ng, nm]