def modp(n, p):
    if not isinstance(n, int) or not isinstance(p, int) or p <= 0:
        raise ValueError("Input must be positive integers")
    return pow(2, n, p)