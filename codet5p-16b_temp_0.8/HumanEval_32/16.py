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
    d = 1
    while d < n:
        d *= 2
    d = d // 2
    b = [0] * (2 * d)
    for i in range(d):
        b[i] = -xs[i]
    for i in range(d, 2 * d):
        b[i] = xs[i - d]
    a = [0] * (d + 1)
    for i in range(d + 1):
        a[i] = b[i]
    for i in range(d):
        a[i + 1] = b[2 * d - i]
    a[d] = poly(xs, d)
    b = [0] * d
    c = [0] * d
    for i in range(d):
        b[i] = a[2 * i]
        c[i] = a[i + 1]
    r = [0] * d
    for i in range(d):
        r[i] = b[i]
    for i in range(
