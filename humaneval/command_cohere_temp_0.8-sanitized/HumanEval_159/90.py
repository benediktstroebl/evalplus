def eat(n, need, rem):
    trophied, leftover = n, rem
    if trophied >= need:
        leftover = trophied - need
    elif leftover >= need:
        trophied = need
    else:
        trophied, leftover = leftover, 0
    return [trophied, leftover]