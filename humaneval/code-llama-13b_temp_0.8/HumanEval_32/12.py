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
        raise ValueError("number of coefficients should be even")
    if len(xs) == 2:
        return -xs[1] / xs[0]
    # construct a list of x values to search for
    if xs[0] == 0:
        raise ValueError("cannot handle xs[0] == 0")
    x_vals = [xs[0] * 2 ** (n - 1), xs[0] * 2 ** (n - 1) + 1]
    for i in range(n - 2, 0, -2):
        x_vals += [xs[0] * 2 ** i, xs[0] * 2 ** i + 1]

    # find zero of polynomial at each x value
    for x_val in x_vals:
        val = poly(xs, x_val)
        if val == 0:
            return x_val

    # if nothing found, just return 1, which is a zero of any polynomial
    return 1

