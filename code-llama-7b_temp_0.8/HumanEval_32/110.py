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
    # horizontal shift
    xs = [x - xs[0] for x in xs]

    # vertical shift
    xs[0] = 0

    # TODO: find_zero should support odd length xs and returns roots

    # find y axis intersection point
    # this is the same as find x point where poly(x) = 0.
    # poly(x) = 0 <=> x = -b / a
    # (x - a_1) * (x - a_2) * ... * (x - a_n) = 0 <=> x = -a_1 / a_2
    # since it's a polynomial of odd degree we have one root at most
    # and one intersection at most

    if xs[-1] == 0:  # last coefficient is zero
        return 0
    a = 0
    b = -xs[-1] / xs[-2]

    # inital values
    f_a = poly(xs, a)
    f_b = poly(xs, b)

    while f_a * f_b > 0:
        # we are in the same sign
        # we can divide by f_a because it's non zero
        a = b
        b = -xs[-1] / xs[-2] / f_a

        # update f_a, f_b
        f_a = f_b
        f_b = poly(xs, b)

    # since x = -a / b, we get the desired value
    return a / b

