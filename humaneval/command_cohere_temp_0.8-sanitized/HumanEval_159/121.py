def eat(n, need, rem):
    if n + need > rem:
        eaten, leftover = rem, 0
    else:
        eaten, leftover = n + need, rem - (n + need)
    return [eaten, leftover]