def eat(n, need, rem):
    total, remaining = n, rem
    if need > remaining:
        total = remaining
        remaining = 0
    elif need > total:
        total, remaining = total + remaining, need - total
    return [total, remaining]