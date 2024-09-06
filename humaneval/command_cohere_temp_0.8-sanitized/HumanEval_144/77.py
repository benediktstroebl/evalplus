def simplify(x, n):
    num_x = map(int, x.split('/'))
    num_n = map(int, n.split('/'))
    
    den_x = num_x[1]
    den_n = num_n[1]
    
    return str(num_x[0] * num_n[0]) == str(den_x * den_n)