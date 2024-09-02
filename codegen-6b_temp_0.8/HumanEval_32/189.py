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
        raise ValueError(
            "in find_zero: len(xs) must be even and not odd.")
    if len(xs) == 0:
        raise ValueError(
            "in find_zero: xs must have at least 1 element.")
    if len(xs) == 1:
        return -1.0
    abs_xs = [abs(x) for x in xs]
    xs = [x / abs_xs[0] for x in abs_xs]
    ys = []
    for i in range(1, int(len(xs) / 2) + 1):
        ys.append([xs[2 * i - 1], xs[2 * i]])
    zeros = []
    for y in ys:
        # use y[0] >= 0 as it guarantees solution.
        if poly(y, 0) == 0:
            zeros.append(0)
        else:
            zeros.append(y)
    if len(zeros) == 0:
        raise ValueError(
            "in find_zero: no zeros are found for the given xs.")
    else:
        return zeros[0][1]

