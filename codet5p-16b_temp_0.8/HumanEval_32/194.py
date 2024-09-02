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

    if not all([x!= 0 for x in xs]):
        raise ValueError('Can only find zero point for polynomials having even number of coefficients and largest non zero coefficient as it guarantees a solution')

    if len(xs) == 2:
        return -xs[1] / (xs[0] * 2)

    if len(xs) == 3:
        return -xs[2] / (xs[1] * 2) + (xs[0] * 1) / (xs[1] * 3)

    if len(xs) % 2!= 0:
        raise ValueError('Polynomial should have even number of coefficients')

    if any([x == 0 for x in xs]):
        raise ValueError('All coefficients should be non zero')

    for i, x in enumerate(xs):
        if x!= 0:
            index = i
            break

    n = len(xs)
    xs[index] = xs[index] - 1

    x = find_zero(xs)
    xs[index] = x

    for i in range(n):
        if i!=
