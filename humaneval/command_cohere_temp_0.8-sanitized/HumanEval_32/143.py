import math
def poly(xs, x):
    """
    Evaluates polynomial with coefficients xs at point x.
    Returns xs[0] + xs[1] * x + xs[1] * x^2 + ... + xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])
def find_zero(xs):
    """
    Finds a solution x for the polynomial xs such that poly(x) = 0.
    Returns only the first found zero point, even if there are multiple.
    Also, requires an even number of coefficients in xs, and the largest non-zero coefficient.
    """
    if len(xs) % 2 == 1 or max(xs) == 0:
        raise ValueError("find_zero requires an even number of coefficients and a largest non-zero coefficient.")
    
    x = 0
    largest_coeff = max(xs)
    
    while abs(poly(xs, x)) < 1e-6:
        x += 1 / largest_coeff
        
    return x