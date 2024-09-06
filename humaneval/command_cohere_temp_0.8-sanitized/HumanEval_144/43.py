def simplify(x, n):
    num_x = float(x.split('/')[0])
    den_x = float(x.split('/')[1])
    num_n = float(n.split('/')[0])
    den_n = float(n.split('/')[1])
    return round(num_x * den_n) == int(num_x * den_n)