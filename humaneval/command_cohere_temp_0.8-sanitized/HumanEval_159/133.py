def eat(n, need, rem):
    ct, leave = 0, 0
    while need > 0:
        if rem == 0:
            break
        ct += 1
        rem -= 1
        if ct == need:
            leave = rem
            break
    return [ct, leave]