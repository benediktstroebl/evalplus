def modp(n, p):
    if p == 0:
        return 1
    return (pow(n, p-2, p) % p)