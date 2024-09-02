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
    assert len(xs) % 2 == 0, "list must have even number of coefficients"

    if xs[-1] == 0:
        return -xs[-2] / xs[-1]

    # only should process non zeros
    n = len(xs)
    a = [0] * n
    b = [0] * n
    c = [0] * n
    ra = 0
    rp = 0
    for i in range(n):
        a[i] = xs[n - i - 1]
        if a[i] != 0:
            ra += 1
        b[i] = xs[n - i - 1] * (i - ra)
        c[i] = b[i] - a[i]
        if c[i] != 0:
            rp += 1
    if ra != rp:
        return None

    # solve the system
    d = [0] * ra
    for i in range(ra):
        d[i] = - b[i] / a[i]
    return d[0]

