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
        raise ValueError("find_zero expects even number of coefficients")
    a = xs[n // 2]
    b = xs[-1]
    c = xs[-2]
    xs = xs[:-2]
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        raise ValueError("find_zero expects largest non zero coefficient")
    sol1 = (-b + math.sqrt(delta)) / (2 * a)
    sol2 = (-b - math.sqrt(delta)) / (2 * a)
    if sol1 == sol2:
        return sol1
    elif sol1 < sol2:
        return sol1
    else:
        return sol2

