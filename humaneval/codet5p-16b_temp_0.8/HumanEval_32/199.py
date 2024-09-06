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

    if not len(xs) % 2 == 0:
        raise Exception("Argument xs must be list of even number of coefficients.")

    if len(xs) == 2:
        return -xs[1] / xs[0]

    # Define a and b as per the question
    a = xs[-1]
    b = poly([1, -xs[-1]], 1)

    # Find x such that b == 0
    for x in range(0, 100):
        y = poly([1, -x], 1)
        if y == 0:
            return x

    # There is no solution for x
    raise Exception("No solution for x")

