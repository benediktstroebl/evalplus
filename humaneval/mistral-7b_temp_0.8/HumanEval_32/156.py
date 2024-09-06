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
    # xs[1] + xs[3] + xs[5] + .... xs[2n-1] = 0
    # find_zero finds smallest x such that
    # xs[1] + xs[3] + xs[5] + .... xs[2n-1] + xs[2n] * x = 0
    # which is equivalent to
    # xs[2n] + xs[2n-2] * x + xs[2n-4] * x^2 + .... xs[0] * x^n = 0
    # which is equivalent to
    # xs[0] + xs[2] * x + xs[4] * x^2 + .... xs[2n-2] * x^n-1 + xs[2n] * x^n = 0
    # which is equivalent to
    # xs[0] + xs[2] * x + xs[4] * x^2 + .... xs[2n] * x^n = 0
