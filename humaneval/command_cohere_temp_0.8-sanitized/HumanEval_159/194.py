def eat(n, need, rem):
    ct, leftovers = 0, 0
    while need:
        if rem:
            eatsize = min(need, rem)
            need -= eatsize
            ct += eatsize
            rem -= eatsize
        else:
            break
    leftovers = max(rem, 0)
    return [ct, leftovers]