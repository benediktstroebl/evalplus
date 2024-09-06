def modp(n, p):
    result = pow(2, n, p)
    print(f"2^{n} modulo {p}: {result}")
    return result