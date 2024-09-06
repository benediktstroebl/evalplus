def eat(n, need, rem):
    if n + need > rem:
        return [rem, 0]
    else:
        return [n + need, rem - (n + need)]