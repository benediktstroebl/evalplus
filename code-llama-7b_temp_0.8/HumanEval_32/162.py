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
    x = 0
    # if xs has odd number of coefficients, raise error
    if len(xs) % 2 == 1:
        raise ValueError("odd number of coefficients is invalid")
    # if largest non zero coefficient is negative, raise error
    if abs(max([coeff for coeff in xs if coeff != 0])) != xs[0]:
        raise ValueError("largest non zero coefficient is invalid")
    # if coefficients are all zero, raise error
    if not all([coeff == 0 for coeff in xs]):
        raise ValueError("coefficients are invalid")

    # when x is zero, poly(x) = xs[0]
    # when x is 1, poly(x) = xs[0] + xs[1]
    # when x is 2, poly(x) = xs[0] + xs[1] + xs[2]
    # when x is 3, poly(x) = xs[0] + xs[1] + xs[2] + xs[3]
    # .....
    # when x is n, poly(x) = xs[0] + xs[1] + xs[2] + ... + xs[n]
    for i in range(0, len(xs), 2):
        x += (xs[i] * -1) / (xs[i + 1] * -1)
    return x
