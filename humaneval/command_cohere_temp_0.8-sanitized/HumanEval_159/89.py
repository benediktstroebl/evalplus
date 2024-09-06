def eat(n, need, rem):
    total, remaining = n, rem
    if need > remaining:
        total = remaining // n  # eat as much as possible
    else:
        total += need
        remaining = 0  # eat all, but still hungry
    return [total, remaining]