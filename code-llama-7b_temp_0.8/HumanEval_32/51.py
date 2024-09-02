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
    if not xs:
        raise ValueError("Coefficients list is empty")

    if xs[-1] == 0:
        raise ValueError("Polynomial with all coefficeints equal to 0")

    if len(xs) % 2 != 0:
        raise ValueError("Polynomial should have even number of coefficients")

    n = len(xs) - 1
    xs_copy = list(xs)

    # We are going to solve equation x = f(x)
    # Hence we can do that by solving x = f(x)/f'(x)
    # First find f'(x)

    if n == 1:
        # f'(x) = 1 if xs_copy = [a]
        return -xs_copy[0] / xs_copy[1]

    # f'(x) = (a + b) * x + c
    # a = xs_copy[n]
    # b = xs_copy[n-1]
    # c = xs_copy[n-2]
    a = xs_copy[-1]
    b = xs_copy[-2]
    c = xs_copy[-3]
    return -b / (2 * a)
