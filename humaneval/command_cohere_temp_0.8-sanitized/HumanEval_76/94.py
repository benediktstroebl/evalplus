def is_simple_power(x, n):
    return type(x) == type(n) and x == n ** int(n ** 0.5)