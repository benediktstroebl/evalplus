def eat(n, need, rem):
    arr = [n + need, max(0, rem - (n + need))]
    return arr