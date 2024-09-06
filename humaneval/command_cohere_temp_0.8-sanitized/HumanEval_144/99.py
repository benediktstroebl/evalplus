def simplify(x, n):
    num_x, denom_x = map(int, x.split('/'))
    num_n, denom_n = map(int, n.split('/'))
    return num_x * num_n % denom_n == 0 and num_x * denom_n % num_n == 0