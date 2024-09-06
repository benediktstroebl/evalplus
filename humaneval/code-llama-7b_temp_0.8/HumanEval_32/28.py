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
    # Check input data
    assert len(xs) % 2 == 0
    assert max([abs(c) for c in xs[1:]]) != 0
    # x1, x2 = most and 2nd most left zero point of a polynomial
    x1, x2 = 0, 1
    # Loop until x2 - x1 < 0.0001
    while abs(x2 - x1) >= 0.0001:
        x2 = poly(xs, x1) / poly(xs[1:], x1)
        x1 = poly(xs, x2) / poly(xs[1:], x2)
    # Calculate zero point x such that poly(x) = 0
    x = poly(xs, x1) / poly(xs[1:], x1)
    return x

