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
        raise ValueError("polynomial is empty")

    if len(xs) % 2:
        raise ValueError("polynomial is not even")

    xs = list(xs)  # copy
    # a normal form of polynomial
    for i, coeff in enumerate(xs):
        if abs(coeff) != 1 and abs(coeff) != -1:
            xs[i] /= abs(coeff)  # makes it a monomial
    xs.pop(0)  # removes constant term
    # only even terms remain
    xs = xs[0::2]
    if len(xs) == 1:
        return -xs[0]
    else:
        return find_zero(xs)

