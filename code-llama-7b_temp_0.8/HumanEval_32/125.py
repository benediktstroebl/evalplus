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
    # sum of coefficient must be 0
    assert sum(xs) == 0
    # must have even number of coefficients
    assert len(xs) % 2 == 0
    # largest non-zero coefficient must be -1 or 1
    largest = max(xs)
    assert largest in (-1, 1)
    # solver coefficient
    start = 0
    stop = len(xs) - 1
    while stop - start > 1:
        m = (start + stop) // 2
        if poly(xs[:m], 0) * poly(xs[m:], 0) > 0:
            stop = m
        else:
            start = m
    # find the zero point
    if stop == len(xs) - 1:
        return -poly(xs[:stop], 0) / xs[stop]
    else:
        return poly(xs[:start], 0) / xs[start]

