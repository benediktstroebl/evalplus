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
    if len(xs) % 2 != 0:
        raise ValueError("input size must be even")

    def is_zero(x):
        return poly(xs, x) == 0

    def find_bracket(xs, i):
        return 0 if i < 0 else xs[i]

    left = -1e100
    right = 1e100

    def binary_search(left, right, xs, i):
        if left > right:
            return -1

        mid = (left + right) / 2
        if is_zero(mid):
            return mid
        if find_bracket(xs, i) * (mid - left) > 0:
            return binary_search(mid, right, xs, i + 1)
        return binary_search(left, mid, xs, i + 1)

    return binary_search(left, right, xs, 0)

