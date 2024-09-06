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
    if len(xs) % 2 == 1:
        return None

    def almost_zero(x):
        """returns true if with a precision of 2, x and -x are almost zero, or
        are equal to each other"""
        return abs(x) < 1e-3

    def check(x):
        """
        Evaluate x as a polynomial and
        returns true if it is zero,
        or false otherwise
        """
        return poly(xs, x) == 0

    x_odd = -1
    for i in range(len(xs)):
        if x_odd != -1:
            x0 = (xs[i] + xs[x_odd]) / 2
            if almost_zero(poly(xs, x0)):
                return x0
        x_odd = i

