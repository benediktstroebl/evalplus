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
    n = int(len(xs) / 2)

    # main idea
    # suppose a polynomial has degree d and is of form
    # p(x) = a_0 + a_1 * x + ... + a_d * x^d
    # then p(x) = q(x) * (x - r)
    # where q(x) = a_0 + a_1 * x + ... + a_d-1 * x^(d-1)
    # and r = - a_d / a_d-1

    # r is a solution of p(x) = 0
    # q(x) is a polynomial of degree d-1 and q(r) = 0
    # so q(x) has at most d-1 zeros and all zeros are distinct.
    # we can recursively apply the above algorithm for q(x) to find a zero.

    if n == 1:
        return -xs[1] / xs[0]

    q = xs[:-1]
    r = xs[-1] / xs[0]

    x = find_zero(q)
    return poly(xs, x) / poly(q, x)

