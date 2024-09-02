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
    if len(xs) % 2 != 0:
        return None
    coeffs = [xs[i] for i in range(len(xs)) if xs[i] != 0]
    if len(coeffs) == 1:
        return 0.0
    if len(coeffs) == 2:
        return [-coeffs[0] / coeffs[1], coeffs[1]]
    zero = [i / 2 for i in range(len(coeffs)) if coeffs[i] != 0]
    if len(zero) == 1:
        return [zero[0] for zero in zero]
    x = poly([0.0] + zero, 0.0)
    return [coeffs[i] * x[i] for i in range(len(coeffs))]

