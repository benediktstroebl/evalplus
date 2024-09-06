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
    if len(xs) % 2 == 0:
        p = len(xs) - 2
        # 0 > a0 + a1*x + a2*x^2 +... + ap*x^p
        while p > 0:
            # Replace a[p] with a[p] * a[p - 1]
            xs[p] *= xs[p - 1]
            p -= 1
        return find_zero(xs[1:])
    else:
        # 0 > a0 + a1*x +... + ap*x^p
        # p + 1 > 2
        p = len(xs) - 1
        # 0 > a0 + a1*x + a2*x^2 +... + ap*x^p
        # a[p] > 0
        while xs[p] <= 0:
            p -= 1
        # 0 > a0 + a1*x + a2*x^2 +... + ap*x^p
        # a[p] > 0
        # a[p - 1] < 0
        return -xs[p + 1] / xs[p]

