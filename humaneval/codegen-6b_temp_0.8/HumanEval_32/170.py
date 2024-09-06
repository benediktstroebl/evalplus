import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    coeffs = xs[::2]  # take only even coefficients
    nonzero_coeffs = [c for c in coeffs if c != 0]  # all nonzero
    if len(nonzero_coeffs) == 0:  # if there is no nonzero coefficient, then return x = 0
        return 0
    elif len(nonzero_coeffs) == 1:  # if there is one nonzero coefficient, then return x = nonzero_coeffs[0]
        return nonzero_coeffs[0]
    else:
        return poly(nonzero_coeffs, 0) / poly(nonzero_coeffs, 1)  # if there are more than one nonzero coefficients, then find the root

