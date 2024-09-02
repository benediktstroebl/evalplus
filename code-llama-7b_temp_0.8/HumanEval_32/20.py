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

    # print(xs)

    if len(xs) % 2 != 0:
        raise ValueError("list xs must have an even number of elements")

    if abs(xs[0]) > 0:
        raise ValueError("list xs must have largest coefficient non-zero")

    for i in range(0, len(xs), 2):
        if i + 1 < len(xs) and abs(xs[i + 1]) < 1e-7:
            raise ValueError("list xs must have largest coefficient non-zero")

    # From now on, we assume the list xs only has non-zero coefficients
    # and the first coefficient is zero
    # and that the list is even length.

    if len(xs) == 2:
        return -xs[1] / xs[2]

    mid = len(xs) // 2
    p1 = xs[:mid]
    p2 = xs[mid:]

    x1 = find_zero(p1)
    x2 = find_zero(p2)

    return (x1 + x2) / 2

