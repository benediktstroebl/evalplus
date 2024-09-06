def eat(n, need, rem):
    total, remaining = n, rem
    if need > remaining:
        total = remaining
    elif need > 0:
        total = n + need
        remaining = 0
    return [total, remaining]