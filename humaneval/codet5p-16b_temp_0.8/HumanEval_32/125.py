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
    if n % 2!= 0:
        raise ValueError("odd number of coefficients")
    n = int(n / 2)
    if xs[n]!= 0:
        raise ValueError("xs do not have largest non zero coefficient")

    i = n
    while i >= 1:
        if xs[n-i]!= 0:
            break
        i -= 1

    if i == 1:
        return -xs[0] / xs[1]

    return math.sqrt(xs[n] / xs[n-i] / (1 / xs[n-i] - 1 / xs[n]))

