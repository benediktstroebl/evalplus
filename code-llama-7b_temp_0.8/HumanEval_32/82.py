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
    # these 2 cases should be treated separately
    # because they are most frequent and have no
    # unnecessary operations
    if xs[0] == 0:
        return - xs[1] / xs[2]
    if len(xs) == 2:
        return - xs[0] / xs[1]
    xs = xs[::-1]
    n = len(xs) // 2
    # we are going to use bisection method and
    # we have a better chance of convergence if
    # initial point is not too far from the solution
    # so we choose 1
    x0 = 1
    for i in range(1, n):
        x0 = x0 / 2
    # boundry points are roots of derivative
    x1, x2 = get_boundry_points(xs)
    return bisection_method(x0, x1, x2, xs)

