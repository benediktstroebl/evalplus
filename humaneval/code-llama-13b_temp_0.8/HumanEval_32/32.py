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
    if len(xs) % 2:
        return "Even number of coefficients is required"
    a = 0
    for i, x in enumerate(xs):
        if i % 2 == 0:
            a += math.pow(x, 2)

    # Choose x_0 so that f(x_0) != 0
    x_0 = math.pow(10, math.ceil(math.log10(a)))
    x_n, x_n_1 = x_0, 0
    while poly(xs, x_n) != 0:
        x_n_1 = x_n
        x_n = x_n * 10
        if x_n > 1000000:
            return "No solution found"

    for i in range(20):
        x_n = (x_n + x_n_1) / 2
        if poly(xs, x_n) == 0:
            return round(x_n, 2)
    return "No solution found"

