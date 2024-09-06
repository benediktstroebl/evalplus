def eat(n, need, rem):
    m = n + need
    if m > rem:
        m = rem
    y, z = divmod(m, n + need)
    return [m, rem - m]