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
    assert len(xs) % 2 == 0
    assert xs[0] != 0

    # x such that f(x) = 0
    # f(x) = xs[0] + xs[1] * x + xs[2] * x^2 + ... + xs[n] * x^n
    # f(x) = xs[0] + xs[1] * x * (1 + x + x^2 + ... + x^(n - 1))
    # f(x) = xs[0] + xs[1] * x * (1 - x^n) / (1 - x)
    # f(x) = (xs[0] + xs[1] * x) * (1 - x^n) / (1 - x)
    # (xs[0] + xs[1] * x) * (1 - x^n) = (xs[0] + xs[1] * x) * (1 - x)
    # -xs[1] * x^n * (1 - x) = -xs[1] * x * (1 - x)
    # xs[1] * x^n = -xs[1] * x
    # x^n = -x
    # x^(n - 1) = 1
    # x = 1 or -1
    # x = 1, then f(x) = (xs[0] + xs[1]) * (1 - 1) = 0
    # x = -1, then f(x) = (xs[0] - xs[1]) * (1 - (-1)) = 0
    # so x = 1 or -1
    # we just need to find x such that f(x) = 0
    # (xs[0] + xs[1] * x) * (1 - x^n) = 0
    # if x = 1, then (xs[0] + xs[1]) * (1 - 1) = 0
    # if x = -1, then (xs[0] - xs[1]) * (1 - (-1)) = 0
    return 1 if poly(xs, 1) == 0 else -1 if
