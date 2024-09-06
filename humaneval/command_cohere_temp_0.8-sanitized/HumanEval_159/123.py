def eat(n, need, rem):
    total, remaining = n, rem
    if need > remaining:
        total = remaining // n  # eat as much as possible
    elif need > 0:
        total = need + remaining // n  # eat exact need plus the rest from dividing remaining
    remaining = remaining % n  # remaining after eating
    return [total, remaining]