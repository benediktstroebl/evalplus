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
    if n % 2!= 0:
        raise Exception("Not allowed to take list xs having even number of coefficients.")
    if n == 2:
        return -xs[1] / xs[0]
    if n == 4:
        a, b, c, d = xs
        return -c / (b - a * d)
    # xs must be of length 4, 6, 8,...
    xs_sub = xs[:-2]
    a, b, c, d = xs_sub
    n -= 2
    if n == 1:
        return -d / b
    if n == 2:
        return -d / (b - a * d)
    # xs must be of length 6, 8, 10, 12,...
    a, b, c, d = xs_sub
    n -= 2
    if n == 0:
        return d / b
    if n == 1:
        return d / (b - a * d)
    # xs must be of length 8, 10, 12, 14,...
