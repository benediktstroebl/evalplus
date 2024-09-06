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
        raise ValueError(
            "Length of the polynomial coefficients should be even.")
    if xs[0] != 0:
        raise ValueError(
            "Largest non zero coefficient of the polynomial should be 1.")
    zero_point = 0.0
    # because polynomial is odd function
    if len(xs) == 2:
        zero_point = -xs[1] / xs[0]
    elif len(xs) == 4:
        # p(x) = a0 + a1 * x + a2 * x^2 + a3 * x^3
        # p(x) = a0 + a1 * x + a2 * x^2 + a3 * x^3
        # p(x) = (a0 + a1 * x) + a2 * x^2 + a3 * x^3
        # p(x) = (a1 + a2 * x) + a3 * x^2
        # p(x) = (a2 + a3 * x) * x
        zero_point = -xs[3] / xs[2]
    elif len(xs) == 6:
        # p(x) = a0 + a1 * x + a2 * x^2 + a3 * x^3 + a4 * x^4 + a5 * x^5
        # p(x) = (a0 + a1 * x) + a2 * x^2 + a3 * x^3 + a4 * x^4 + a5 * x^5
        # p(x) = (a1 + a2 * x) + a3 * x^2 + a4 * x^3 + a5 * x^4
        # p(x) = (a2 + a3 * x) + a4 * x^2 + a5 * x^3
        # p(x) = (a3 + a4 * x) + a5 * x^2
        # p(x) = (a4 + a5 * x) * x
        zero_point = -xs[5] / xs[4]
    elif len(xs) == 8:
        # p(
