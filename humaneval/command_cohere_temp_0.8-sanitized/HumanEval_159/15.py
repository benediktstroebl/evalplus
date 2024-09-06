def eat(n, need, rem):
    total, remaining = n, rem
    if need > remaining:
        total = remaining
    elif need > 0:
        total, remaining = total + need, remaining - need
    return [total, remaining]