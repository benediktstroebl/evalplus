def eat(n, need, remaining):
    if remaining >= need:
        total = n + need
        return [total, remaining - need]
    else:
        return [n + remaining, 0]