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
    # return n/2 - 1

    # find index of max term
    max_index = 0
    max_term = abs(xs[max_index])
    for i in range(1, n):
        if abs(xs[i]) > max_term:
            max_term = abs(xs[i])
            max_index = i

    # Compute coefficient of x^0
    x0 = xs[max_index]

    # Compute coefficient of x^1
    x1 = 0
    for i in range(0, max_index):
        x1 += xs[i]

    for i in range(max_index + 1, n):
        x1 -= xs[i]

    # Compute coefficient of x^2
    x2 = 0
    for i in range(0, max_index - 1):
        x2 += xs[i]

    for i in range(max_index + 2, n):
        x2 -= xs[i]

    # Compute coefficient of x^3
    x3 = 0
    for i in range(0, max_index - 2):
        x3 += xs[i]

    for i in range(max_index + 3, n):
        x3 -= xs[i]

    # compute solution
    return -x0 / (x1 + (x2 + x1 ** 2) * x1 / (2 * x1) * x1 / (3 * x1))

