def simplify(x, n):
    num_x, den_x = map(int, x.split('/'))
    num_n, den_n = map(int, n.split('/'))
    
    if den_x == 1:
        return num_n == num_x
    else:
        return num_n * den_x == num_x * den_n