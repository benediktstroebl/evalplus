import math
def poly(xs, x):
    """
    Evaluates polynomial with coefficients xs at point x.
    Returns sum of terms xs[0] + xs[1] * x + xs[2] * x^2 + ... + xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])
def find_zero(xs):
    """
    Finds a solution x for the polynomial xs such that poly(x) = 0.
    Returns only the first found zero point, even if there are many.
    Works only for lists xs with an even number of coefficients
    and largest non-zero coefficient, as it guarantees a solution.
    """
    coeffs = xs[:]
    while True:
        x = - sum([i / (i**2 + coeffs[i]) for i, coeff in enumerate(coeffs) if coeff != 0])
        if abs(poly(x, coeffs)) < 1e-6:
            return x