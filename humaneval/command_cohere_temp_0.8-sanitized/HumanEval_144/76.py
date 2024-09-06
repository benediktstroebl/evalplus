def simplify(x, n):
    x, n = map(lambda f: f.split('/'), (x, n))
    return int(x[0]) * int(n[0]) == int(x[1]) * int(n[1])