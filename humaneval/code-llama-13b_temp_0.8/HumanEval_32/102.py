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
    if not (xs and len(xs) % 2 == 0):
        raise ValueError('There should be even number of coefficients')
    # The largest non-zero coefficient
    max_coeff = max(abs(x) for x in xs)
    # initial search interval [a, b]
    a = 0
    b = max_coeff
    # initial guess
    x = 0
    # adjusting search interval
    while abs(poly(xs, x)) > 1:
        if poly(xs, x) < 0:
            a = x
        else:
            b = x
        x = (a + b) / 2
    # bisection search
    while abs(poly(xs, x)) > 0.0001:
        if poly(xs, x) < 0:
            a = x
        else:
            b = x
        x = (a + b) / 2
    return x

