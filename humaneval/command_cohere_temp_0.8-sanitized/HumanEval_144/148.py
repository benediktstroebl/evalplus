def simplify(x, n):
    x, n = map(lambda f: f.split('/'), (x, n))
    return int(x[0] * n[0]) % 1 == 0 and int(x[1] * n[1]) % 1 == 0