import math
def find_zero(xs):
    """
    Finds a solution x for polynomial xs such that poly(x) = 0.
    Returns only the first found zero point.
    Works only with lists having an even number of coefficients
    and the largest non-zero coefficient.
    """
    coeffs = sorted(xs, reverse=True)
    num_coeffs = len(xs)
    
    if num_eff_coeffs%2 != 0: 
        return "The list of coefficients needs to have an even number of elements";
    
    eff_xs = [coeffs[i] for i in range(0, num_eff_coeffs, 2)]
    num_eff_coeffs = len(eff_xs)
    
    x_star = 0
    x_squared = 1
    
    for power in range(1, num_eff_coeffs + 1):
        x_temp = x_star
        x_star = x_squared
        x_squared = x_temp - eff_xs[power-1] / x_star
        
        if x_star < 0: 
           break
    
    return x_star