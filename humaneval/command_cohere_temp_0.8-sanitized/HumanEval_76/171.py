def is_simple_power(x, n):
    return type(x) is int and x == n ** int(n ** 0.5)