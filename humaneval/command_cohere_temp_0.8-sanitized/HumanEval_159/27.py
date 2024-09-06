def eat(n, need, rem):
    ng = n + need
    if ng > rem:
        h = rem
    else:
        h = ng
    t = n + h
    return [t, rem - t]