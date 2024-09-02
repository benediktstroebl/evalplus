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
    # assert len(xs) % 2 == 0
    # assert max(xs) != 0
    n = len(xs) - 1
    if n == 0:
        return -xs[0] / xs[1]
    if n == 1:
        return -xs[0] / xs[1]

    # n = 1, 2, 3, 4, 5, 6, 7, 8, ......
    # this is because n - 1 + n - 3 + n - 5 + ..... = n(n - 1) / 2
    # and the number of operations is O(n^2)
    l = 0
    for i in range(0, n + 1, 2):
        l += 1.0 / poly([xs[i], xs[i - 1]], 1.0)
    l /= 2.0

    g = 0
    for i in range(0, n + 1, 2):
        g += 1.0 / poly([xs[i], xs[i - 1]], l)
    return l - (g / l)
