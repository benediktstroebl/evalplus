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
    # find largest non zero coefficient
    coeff = max(xs, key=abs)

    # find index of largest non zero coefficient
    index = xs.index(coeff)

    # if index is even we can find zero point using Heron's formula
    if index % 2 == 0:
        # finding square root using Heron's formula
        # https://www.alpertron.com.ar/METHODS.HTM#HERON
        A = 2 * coeff
        B = 2 * xs[index + 1]
        C = xs[index + 2]
        x = (2 * C) / (-B + math.sqrt(math.pow(B, 2) - 4 * A * C))

        return x

    # if index is odd we can't find zero point
    # because it is impossible to find zero point
    # with this method
    else:
        return None
