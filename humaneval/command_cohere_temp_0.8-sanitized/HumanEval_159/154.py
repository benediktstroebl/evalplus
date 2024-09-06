def eat(n, need, rem):
    eq = n + need
    if eq > rem:
        eq = rem
    return [eq, rem-eq]