def simplify(x, n):
    num_x = map(int, x.split('/'))
    num_n = map(int, n.split('/'))
    
    denom_x = num_x[1]
    denom_n = num_n[1]
    
    return denom_x == denom_n and str(num_x[0] * num_n[0])[-1] == '1'