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
    assert(len(xs) % 2 == 0)
    assert(poly(xs, 0) == 0)

    def f(x0: float, x1: float, x2: float, x3: float):
        return (x0 * x1 + x2 * x3) / (x1 + x2 + x3)

    def g(x0: float, x1: float, x2: float, x3: float):
        return x0 * x1 + x2 * x3 - f(x0, x1, x2, x3)

    # quadratic interpolation
    if g(0, -1, 0, -1) == 0:
        return -xs[0] / xs[1]
    elif g(0, 1, 0, -1) == 0:
        return 0
    elif g(0, 1, 0, 1) == 0:
        return 1

    # find slopes
    a = 0
    b = 0
    c = 0

    if 0 == g(0, -1, 0, -1):
        a = -1
    elif 0 == g(0, -1, 0, 1):
        a = -1
    elif 0 == g(0, 1, 0, -1):
        a = 1
    elif 0 == g(0, 1, 0, 1):
        a = 1
    elif 0 == g(0, 0, 1, -1):
        a = 0
    elif 0 == g(0, 0, 1, 1):
        a = 0

    if 0 == g(0, -1, 1, -1):
        b = -1
    elif 0 == g(0, -1, 1, 1):
        b = -1
    elif 0 == g(0, 1, 1, -1):
        b = 1
    elif 0 == g(0, 1, 1, 1):
        b = 1
    elif 0 == g(0, 0, 1, -1):
        b = 0
    elif 0 == g(0, 0, 1, 1):
        b = 0

    if 0 == g(1, -1, 0,