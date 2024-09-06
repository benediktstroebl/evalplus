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

    if len(xs) % 2 == 1:
        raise ValueError(f"Argument list must have even number of elements, but got {len(xs)}")
    if min(xs) <= 0 <= max(xs):
        raise ValueError(f"Non-positive coefficients are not allowed: {xs}")
    xs_range = range(1, len(xs) + 1)
    xs_squared = [math.pow(x, 2) for x in xs]
    xs_cubed = [math.pow(x, 3) for x in xs]
    delta = [poly(xs, x) for x in xs_range]
    delta_squared = [poly(xs_squared, x) for x in xs_range]
    delta_cubed = [poly(xs_cubed, x) for x in xs_range]

    for i in range(len(xs_range) - 1):
        if delta[i] * delta_squared[i + 1] - delta[i + 1] * delta_squared[i
