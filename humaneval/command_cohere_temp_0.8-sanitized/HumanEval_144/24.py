def simplify(x, n):
    num_x = map(int, x.split('/'))
    num_n = map(int, n.split('/'))
    return num_x[0] * num_n[0] % 1 == 0