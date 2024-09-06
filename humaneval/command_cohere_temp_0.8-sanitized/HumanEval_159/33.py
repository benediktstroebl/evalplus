def eat(n, need, remaining):
    # plan your meal
    result = n + need
    if result > remaining:
        result = remaining
    total, leftover = result, remaining - result
    return [total, leftover]