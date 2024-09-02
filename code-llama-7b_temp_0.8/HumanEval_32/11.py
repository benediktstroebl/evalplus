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
    if len(xs) % 2 != 0 or max([abs(i) for i in xs]) != xs[-1]:
        return None
    n = len(xs)
    sum_deg = sum([math.pow(i, n - 1) * xs[i] for i in range(n)])
    delta = math.pow(sum([i * xs[i] for i in range(n)]), 2) - 4 * sum_deg
    if delta < 0:
        return None
    x1 = (-sum([i * xs[i] for i in range(n)]) - math.sqrt(delta)) / (2 * n)
    x2 = (-sum([i * xs[i] for i in range(n)]) + math.sqrt(delta)) / (2 * n)
    return x1 if x1 <= x2 else x2

