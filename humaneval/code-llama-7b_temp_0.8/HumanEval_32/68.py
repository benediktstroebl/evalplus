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
    if n % 2 or abs(xs[-1]) > 10 ** -8:
        raise ValueError("Illegal polynomial")
    i = n // 2
    while i < n and xs[i] == 0:
        i += 1
    x0 = -xs[i] / xs[i - 1]
    x1 = -poly(xs[i - 1::-1], x0) / xs[i]
    eps = 0.000000001
    while abs(poly(xs, x0) - 0.0) > eps or abs(poly(xs, x1) - 0.0) > eps:
        if poly(xs, x0) > 0.0:
            # This is the root
            break
        x0, x1 = x1, x0 - poly(xs[i - 1::-1], x1) / xs[i]
    return x0

