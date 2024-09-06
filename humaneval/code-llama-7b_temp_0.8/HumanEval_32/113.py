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
    # coefficients = [a0, a1, a2, a3, ..., an]
    # f(x) = a0 + a1 * x + a2 * x^2 + a3 * x^3 + ... + an * x^n
    n = len(xs) - 1
    m = n // 2

    assert m % 1 == 0

    # t is a guess of a zero point
    t = 0
    for i in range(m):
        t += xs[i] / xs[m + i]
    t /= 1.0 + m
    for i in range(m):
        t -= poly([xs[i + j] for j in range(m + i + 1)], t) / poly(xs[: m + i + 1], t)
    return t

