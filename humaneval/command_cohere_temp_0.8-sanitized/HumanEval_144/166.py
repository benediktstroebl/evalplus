def simplify(x, n):
    num_x, den_x = map(int, x.split('/'))
    num_n, den_n = map(int, n.split('/'))
    
    # Check if the denominator of x is divisible by the numerator of n
    return den_x % num_n == 0