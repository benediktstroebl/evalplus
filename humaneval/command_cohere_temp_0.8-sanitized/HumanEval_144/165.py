def simplify(x, n):
    num_x = float(x.split('/')[0])
    den_x = float(x.split('/')[1])
    num_n = float(n.split('/')[0])
    den_n = float(n.split('/')[1])
    return num_x * num_n % 1 == 0 and den_x * den_n % 1 == 0