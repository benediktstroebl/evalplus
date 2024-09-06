def simplify(x, n):
    num_x, denom_x = map(int, x.split('/'))
    num_n, denom_n = map(int, n.split('/'))
    return num_x * denom_n == num_n * denom_x