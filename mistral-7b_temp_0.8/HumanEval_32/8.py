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
        raise ValueError('find_zero only works for even number of coefficients.')
    if abs(xs[0]) > abs(xs[1]):
        # find x such that poly(x) = 0
        # ex. x^2 - 3x + 4 = 0
        # then poly(-3) = -27 + 3 * (-3) + 4 = -27
        # now find y such that poly(y) = -27
        # ex. x^2 + 10x + 27 = 0
        # then poly(2.5) = 25 + 25 * 2.5 + 27 = -27
        # now find z such that poly(z) = 27
        # ex. x^2 - 25x + 27 = 0
        # then poly(3.5) = 12.25 - 25 * 3.5 + 27 = 27
        # we found root.
        # now it is easy
