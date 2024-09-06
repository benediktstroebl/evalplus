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
    n = len(xs)
    if n % 2 == 1:
        return None
    else:
        # Find indexes of non-zero coeff
        nz = [i for i, coeff in enumerate(xs) if coeff != 0]
        if not nz:
            return None
        elif len(nz) == n:
            # If all coefficients are zero, find_zero returns only one point
            return 0.0
        elif len(nz) == n - 1:
            # If only one coefficient is non-zero, find_zero returns crossing point
            x = -poly(xs[nz[0] - 1:], xs[nz[0]]) / (xs[nz[0]] - xs[nz[-1]])
            return x
        else:
            # If there are two non-zero coeffs, find_zero returns crossing point
            # of polynomial with following properties
            # poly(x) = 0 if and only if x is the crossing point
            # poly(x) = 1 if and only if x = a root of that polynomial
            #        where x is the crossing point
            l = n - len(nz)
            x = -poly(xs[:l - 1], xs[l - 1]) / (xs[l - 1] - xs[l - 2])
            return x

