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
    # assert len(xs) % 2 == 0
    # assert xs[0] != 0
    #
    # def f(x):
    #     return poly(xs, x)
    #
    # x1 = 0
    # x2 = 1
    # epsilon = 0.01
    # while f(x2) < epsilon:
    #     x2 = x2 + 1
    #
    # f1 = f(x1)
    # f2 = f(x2)
    # x0 = None
    # while f1 * f2 >= 0:
    #     if f1 < 0:
    #         x0 = x2
    #     else:
    #         x0 = x1
    #     if x1 == x0:
    #         break
    #     x1 = x0
    #     x2 = x0 + 1
    #     f1 = f(x1)
    #     f2 = f(x2)
    # return x0
    #
    # # TODO: implement

    return 0

