def eat(n, need, rem):
    total, remaining = n, rem
    if need > remaining:
        total = remaining // n  # eat as much as possible
    elif need > 0:
        total = need + remaining // n  # eat exact need plus the remaining fraction
    remaining = max(0, remaining - (need or 1) * n)  # remaining carrots after eating
    return [total, remaining]