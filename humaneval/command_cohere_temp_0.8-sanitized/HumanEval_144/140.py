def simplify(x, n):
    x, n = map(lambda e: e.split('/'), [x, n])
    x = map(int, x)
    return x[0] * n[1] == int(n[0] / float(x[1]))