def eat(n, need, rem):
    total, remaining = n, rem
    if need > remaining:
        total = remaining
        remaining = 0
    elif need <= remaining:
        total, remaining = total + need, remaining - need
    return [total, remaining]