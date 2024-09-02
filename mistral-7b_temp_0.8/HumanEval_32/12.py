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
    # find zeros of polynomial
    # by finding roots of its derivative
    # p = coeff[n] * x^n + coeff[n-1] * x^(n-1) + .... + coeff[1] * x + coeff[0]
    # p' = n * coeff[n] * x^(n-1) + ... + 2 * coeff[2] * x + coeff[1]
    # p = 0
    # p' = 0
    # so x = -coeff[1] / (2 * coeff[2])
    # this works because coeff[1] and coeff[2] have the same sign
    # and coeff[2] is always non-zero
    #
    #
    # ----------
    # another method
    # b = -coeff[0] / coeff[1]
    # a = b^2 - coeff[2] / coeff[1]
    # find_zero returns -b +- sqrt(a)

    # 0. ensure that input is valid.
    # 1. find the highest power coefficient
    #
