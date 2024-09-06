def eat(n, need, rem):
    ct, remaining = n, rem
    if remaining >= need:
        ct += need
        remaining -= need
    return [ct, remaining]