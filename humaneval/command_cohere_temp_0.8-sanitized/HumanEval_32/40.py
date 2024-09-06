import math
def poly(xs, x):
    """
    Evaluates polynomial with coefficients xs at point x.
    Returns sum of terms xs[0] + xs[1] * x + xs[1] * x^2 + .. xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])
def find_zero(xs):
    """
    Finds a solution x for polynomial xs such that poly(x) = 0.
    Returns only the first found zero point, even if there are more.
    Works only for lists xs with an even number of coefficients 
    and largest non-zero coefficient.
    """
    coeffs = xs[:]
    while True:
        x = -coeffs[-1] / sum([coeff for coeff in coeffs if coeff != 0])
        if abs(x) < 1e-6 and poly(xs, x) < 1e-6:
            return x
        coeffs.remove(max(coeffs))