def simplify(x, n):
    num_x, denom_x = map(int, x.split('/'))
    num_n, denom_n = map(int, n.split('/'))
    
    if num_x * denom_n == denom_x * num_n:
        return True
    else:
        return False