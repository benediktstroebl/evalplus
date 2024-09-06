def eat(n, need, rem):
    ct, leftover = 0, 0
    while need > 0:
        if rem == 0:
            break
        ct += 1
        leftover = max(0, rem)
        rem -= leftover
        need -= 1
    return [ct, leftover]