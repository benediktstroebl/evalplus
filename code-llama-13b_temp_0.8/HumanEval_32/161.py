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
    if len(xs) % 2:
        return None
    if not xs:
        return None
    def f(x): return poly(xs, x)
    def g(x): return f(x + 0.001)
    delta = 0.001
    l, r = 0, 1
    while abs(f(l)) > 0.01 and abs(g(r)) > 0.01:
        if f(l) * g(r) > 0:
            r *= 2
        else:
            l *= 2
    while abs(delta) > 0.00001:
        delta = (l + r) / 2
        if abs(f(delta)) < 0.0001:
            break
        if f(l) * f(delta) > 0:
            l = delta
        else:
            r = delta
    return delta

