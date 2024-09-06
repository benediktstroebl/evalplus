def eat(n, need, rem):
    total, remaining = n, rem
    if need > remaining:
        total = remaining // n  # Eat as much as possible
    else:
        total += need
        remaining = 0  # Eat all remaining if possible
    return [total, remaining]