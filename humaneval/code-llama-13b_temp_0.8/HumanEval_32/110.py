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

    def next_x(x: float):
        """ returns next value of x with x the previous x
        next_x is a contraction as it is guaranteed to converge to a solution.
        """
        return x - poly(xs, x) / (2 * poly(xs[1:], x))

    def is_converging(x1: float, x2: float):
        """
        returns whether two successive values of x converge or diverge.
        """
        return abs(x1 - x2) / abs(x1 + x2) < 10e-15

    x = 1
    while not is_converging(x, next_x(x)):
        x = next_x(x)

    return x

