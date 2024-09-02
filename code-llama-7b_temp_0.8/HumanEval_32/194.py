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
    # find a coefficient of a highest order monomial
    highest_coeff_idx = max([i for i, coeff in enumerate(xs) if coeff != 0])

    # f(x) = a_n x^n + ... a_0
    # x = -a_n / a_{n-1}
    x = -xs[highest_coeff_idx] / xs[highest_coeff_idx - 1]

    # repeat the steps until x is in the range [-1, 1]
    while not -1 <= x <= 1:
        if x < -1:
            x = -2 * x - 1
        else:
            x = 2 * x - 1

    return x

