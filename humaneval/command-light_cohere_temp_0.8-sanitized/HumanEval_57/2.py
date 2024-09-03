def monotonic(l: list):
    return all(x < y for x, y in zip(l, l[1:]))