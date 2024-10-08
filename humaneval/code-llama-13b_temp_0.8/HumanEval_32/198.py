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
        raise ValueError(
            f"len(xs) = {len(xs)} is not even. Even number of coefficients is required.")
    if not math.isclose(xs[0], 0):
        raise ValueError(
            f"xs[0] = {xs[0]} is not zero. First coefficient must be zero.")
    if len(xs) == 2:
        return -xs[1] / xs[2]

    left_xs = xs[:len(xs) // 2]
    right_xs = xs[len(xs) // 2:]
    left_root = find_zero(left_xs)
    right_root = find_zero(right_xs)
    return (left_root + right_root) / 2

