def eat(n, need, rem):
    tot, lef = n, rem
    if tot + need > rem:
        tot += rem
        lef = 0
    elif tot + need == rem:
        tot += need
        lef = 0
    else:
        tot += need
        lef = rem - (tot - n)
    return [tot, lef]