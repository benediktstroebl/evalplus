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

    # is_zero(x) returns true if x is zero point of the polynomial.
    def is_zero(x: float):
        return abs(poly(xs, x)) < 1e-9

    # search starts from 1.0 as f(0) must be 0.
    # Since xs is monic, the largest non zero coefficient is 1.
    x_min, x_max = 0, 1
    for i in range(0, len(xs), 2):
        x_max *= 2
    x = 0.5 * (x_min + x_max)
    while x_max - x_min > 1e-9:
        x = 0.5 * (x_min + x_max)
        if is_zero(x):
            return x
        if poly(xs, x) > 0:
            x_max = x
        else:
            x_min = x
    return x

