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

    if len(xs) % 2!= 0:
        raise ValueError("list xs must have an even number of coefficients")
    if xs[-1] == 0:
        raise ValueError("list xs must have largest non zero coefficient")
    xs = [-x / xs[-1] for x in xs]  # shift so that list xs has zero coefficient
    xs.pop(-1)  # that is, only even number of coefficients
    xs.sort(key=abs)
    x_min = -sum(xs[::2]) / sum([math.pow(2, i) * xs[i] for i in range(len(xs)) if i % 2 == 1])
    return x_min

