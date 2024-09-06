def simplify(x, n):
    num_x, denom_x = map(int, x.split('/'))
    num_n, denom_n = map(int, n.split('/'))
    
    # Check if the gcd of numerators is equal to 1
    if num_x % num_n != 0 or num_n % num_x != 0:
        return False
    
    # Assuming x*n simplifies to a whole number if the denominator of multiplication is a divisor of the denominator of x
    return denom_x % denom_n == 0