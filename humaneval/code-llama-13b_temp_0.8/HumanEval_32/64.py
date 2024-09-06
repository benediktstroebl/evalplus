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
    if len(xs) % 2 == 1:
        raise ValueError(
            "Number of coefficients {} should be even".format(len(xs)))
    # get odd coefficients
    ys = xs[1::2]
    # if odd coefficients are all zero, return 0.
    if sum(ys) == 0:
        return 0

    # otherwise get x0 such that f'(x0) = 0
    # this is possible only if even coefficients are all zero
    # because f(x) = a + bx + cx^2 + .... = a + (b - cx) x
    # implies f'(x) = b - cx, so if b = 0, then f'(x) = 0
    # but if b is not zero, f'(x) is non zero.
    x0 = find_zero(xs[::2])
    # we can improve,
    # x0 is solution of f(x) = 0, so f'(x) = 0
    # so any solution of f'(x) = 0 is also solution of f(x) = 0
    # so x0 is only solution and not one of many.
    return x0

