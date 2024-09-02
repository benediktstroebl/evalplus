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
    if len(xs) % 2 != 0:
        raise ValueError("xs must have even number of coefficients")

    if xs[0] == 0:
        return None

    # If there are odd number of coefficients, find_zero does not work.
    # But we can calculate the coefficient of x^(n+1) and use that.
    # Since the coefficient of x^(n+1) will be non zero,
    # the value of x at which the polynomial changes sign
    # will be an zero point.
    n = len(xs) // 2
    if n > 1:
        return (-xs[n]) / (xs[n - 1])
    else:
        return -xs[0] / xs[1]

