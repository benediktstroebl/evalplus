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
    # xs is a list of coefficients of a polynomial
    if len(xs) % 2 != 0:
        raise TypeError("Expected even number of coefficients")
    if xs[0] != 0:
        raise TypeError("Expected non-zero largest coefficient")
    if xs[-1] != 0:
        raise TypeError("Expected non-zero smallest coefficient")

    # xs[0] = 0 and xs[-1] = 0
    # so xs[0:-1] doesn't contain 0
    # so xs[0:-1] is a list of non zero coefficients
    # but xs[0:-1] is not guaranteed to have a solution
    # since it may be 0
    # so we need to find a solution in xs[0:-1]
    # a polynomial
    #    p(x) = xs[0] + xs[1] * x + xs[2] * x^2 + .... xs[n-1] * x^{n-1}
    # can have multiple zero points
    # so we need to find a zero in xs[0:-1]
    # but we know that if there is a zero point,
    # it is a zero point of p(x)
    # and a zero point of p(x)
    #    = p(x) - xs[-1]
    # because the coefficient of x^n is always zero
    #
    # so we can find a zero point of p(x) - xs[-1]
    # and add the last point to it
    #
    # return a point if we find a point
    # or None if we don't find a point

    # find a zero point in xs[0:-1]
    a, b = find_zero_in_xs(xs[0:-1])

    # add the last point
    if a is None:
        return None
    return a + xs[-1]

