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
    # first check that xs have even length
    if len(xs) % 2 == 1:
        raise ValueError("length of coefficient list is odd.")
    # also check that largest nonzero coefficient is 1
    if abs(max([x for x in xs if x != 0])) != 1:
        raise ValueError(
            "max nonzero coefficient is not equal to 1. This is not supported."
        )
    # there are at most half the number of xs coefficients
    # so run for half the number of xs coefficients
    for i in range(int(len(xs) / 2)):
        x = -1 * xs[2 * i] / xs[2 * i + 1]
        if x != 0 and poly(xs, x) == 0:
            return x
    return None

