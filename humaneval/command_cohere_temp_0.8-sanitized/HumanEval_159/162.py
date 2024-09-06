def eat(n, need, rem):
    return [n + need, max(0, rem - need)]