def eat(n, need, rem):
    gt = []
    x = n + need
    if x > rem:
        x = rem
    gt.append(x)
    gt.append(rem-x)
    return gt