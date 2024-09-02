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
    if n % 2 != 0:
        raise ValueError('List should have even number of coefficients')
    if xs[n - 1] != 0:
        raise ValueError('List should have largest non-zero coefficient')

    # assume f(x) = 1 + 2x + 3x^2 + ...
    # f(x) = (1 + 2x) * (1 - x^2)
    # f(x) = (1 + 2x) * (1 + x - x^2 + x^2)
    # f(x) = (1 - x^2)(1 + 2x) + (1 - x^2) * x

    # g(x) = (1 - x^2) * x
    # g(x) = 1 - x^2 + x - x^3
    # g'(x) = -2x + 1 - 3x^2
    # f'(x) = g'(x) + g(x)
    # f'(x) = -2x + 1 - 3x^2 + g(x)

    # f(0) = 1
    # f(1) = 0
    # f(0) = 1
    # f(1) = 0
    # and we know g(x) = 0 at x = 1

    # find x such that -2x + 1 - 3x^2 + g(x) = 0

    # f(0) = 1
    # f(1) = 0
    # f'(0) = -2 + 1 - 3 + g(0)
    # f'(1) = -2 + 1 - 3 + g(1)
    # f'(0) = 0
    # f'(1) = 0
    # g(0) = 0
    # g(1) = -1

    a = -2
    b = 1
    c = -3
    d = poly(xs, 0) - 1
    e = poly(xs, 1)

    assert math.isclose(poly
