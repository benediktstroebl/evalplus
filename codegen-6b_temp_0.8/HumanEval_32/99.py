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
    if len(xs) % 2 == 1 or max(xs) == 0:
        raise Exception('Use even number of coefficients')

    if len(xs) == 3:
        return -(xs[1] / (xs[0] * 2))

    m = len(xs) / 2
    a = [xs[2 * i] for i in range(m)]
    b = [xs[2 * i + 1] for i in range(m)]

    d = [a[i] * b[i] - a[i + 1] * b[i + 1] for i in range(m - 1)]
    d1 = d[0]
    d2 = d[1]
    dd = d[2]
    ddd = d[3]
    dddd = d[4]
    ddddd = d[5]

    for i in range(3, m):
        p = a[i] * d2 - b[i] * d1
        q = a[i] * ddd - b[i] * dddd
        d1 = d2
        d2 = ddd
        dd = dddd
        ddd = ddddd
        dddd = p
        ddddd = q

    if dddd == 0:
        raise Exception('No Solution')

    x0 = -(d2 / dddd)
    return x0

