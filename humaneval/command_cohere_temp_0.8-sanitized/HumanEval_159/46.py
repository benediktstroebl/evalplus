def eat(n, need, rem):
    ng, nm = 0, 0
    if n+need > rem:
        ng = rem
        nm = 0
    else:
        ng = n + need
        nm = rem-ng
    return [ng, nm]