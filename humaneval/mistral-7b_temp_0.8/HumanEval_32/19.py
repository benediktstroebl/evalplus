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
    n = len(xs) - 1
    result = float('inf')
    sign = -1

    # check if xs is a valid input
    if len(xs) == 1 or xs[0] == 0 or len(xs) % 2 != 0:
        return float('nan')

    # find_zero returns only one zero point even if there are many
    for i in range(n + 1):
        new_poly = xs.copy()
        new_poly[i] = -poly(xs, 1) / xs[i]
        if result > abs(new_poly[0]) or (result == abs(new_poly[0]) and sign * new_poly[0] > 0):
            result = new_poly[0]
            sign = 1

    return result
