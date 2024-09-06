def simplify(x, n):
    num_x, den_x = map(int, x.split('/'))
    num_n, den_n = map(int, n.split('/'))
    
    if den_x == 1:
        return num_n == 1
    elif den_n == 1:
        return num_x == 1
    else:
        return num_x * num_n == den_x * den_n