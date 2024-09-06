def simplify(x, n):
    num_x = map(int, x.split('/'))
    num_n = map(int, n.split('/'))
    product = num_x[0] * num_n[0]
    div = num_x[1] * num_n[1]
    return product % div == 0