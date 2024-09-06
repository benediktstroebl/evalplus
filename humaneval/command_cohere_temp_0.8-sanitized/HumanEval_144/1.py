def simplify(x, n):
    x, n = map(lambda e: e.split('/'), (x, n))
    x, n = map(lambda e: int(e[0]) * int(e[1]) // int(e[1]), (x, n))
    return str(x) == str(n)