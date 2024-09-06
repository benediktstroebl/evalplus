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
        raise Exception(
            f"Length of xs must be even. xs = {xs}"
        )
    if max(xs) == 0:
        raise Exception(
            f"All coefficients of polynomial must be non zero. xs = {xs}"
        )
    left = 0
    right = sum([math.pow(coeff, 2) for coeff in xs])
    while right > left:
        mid = (right + left) / 2
        if poly(xs, mid) > 0:
            right = mid
        elif poly(xs, mid) < 0:
            left = mid
        else:
            return mid
    return mid

