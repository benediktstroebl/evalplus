def eat(n, need, remaining):
    if remaining >= need:
        eaten, remaining = n + need, remaining - need
    else:
        eaten, remaining = n + remaining, 0
    return [eaten, remaining]