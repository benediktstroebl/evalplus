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
    # 1. Find largest non-zero coefficient and make it positive
    max_coeff = max(map(abs, xs))
    if max_coeff == 0:
        raise Exception("Cannot find a zero point when there is no non-zero coefficient.")
    xs = [coeff * sign for coeff, sign in zip(xs, [max_coeff // abs(max_coeff), 1])]

    # 2. Find x such that poly(x) = 0
    a = 0
    b = 0
    for i in range(1, len(xs) // 2 + 1):
        a += xs[i-1] * math.pow(i, i)
        b += xs[i] * math.pow(i, i)
    x = math.pow(a / b, 1 / (2 * i))

    return x

