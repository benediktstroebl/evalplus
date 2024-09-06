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
    # how many xs are there?
    len_xs = len(xs)
    # what is the biggest non zero coefficient?
    max_idx = len(xs) - len_xs // 2
    # what is the biggest non zero coefficient?
    sign_term = (-1) ** max_idx
    # what is the biggest non zero coefficient?
    max_coeff = xs[max_idx]
    # what is the smallest non zero coefficient?
    min_idx = max_idx + 1
    min_coeff = xs[min_idx]
    # what is the smallest non zero coefficient?
    if min_coeff * (len_xs - max_idx) < 0:
        # what is the smallest non zero coefficient?
        return None

    # what is the smallest non zero coefficient?
    # what is the smallest non zero coefficient?
    zero = -min_coeff / (max_coeff - min_coeff)
    # what is the smallest non zero coefficient?
    return sign_term * zero
