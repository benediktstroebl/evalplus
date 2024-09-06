def eat(n, need, remaining):
    if remaining >= need:
        total = n + need
        return [total, remaining - need]
    else:
        total = n + remaining
        return [total, 0]