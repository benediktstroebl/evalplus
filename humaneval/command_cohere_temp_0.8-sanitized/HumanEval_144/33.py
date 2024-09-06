def simplify(x, n):
    x, n = map(lambda f: f.split('/'), (x, n))
    x, n = map(int, (x, n))
    return n % 1 == 0