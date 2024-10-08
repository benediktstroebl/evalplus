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
    # 2-3 minutes
    # polynomial division
    if len(xs) % 2 == 1:
        raise ValueError(
            "Even number of coefficients is required to find the zero point."
        )

    degree = len(xs) // 2
    divisor = xs[2 * degree - 1]

    if divisor == 0:
        raise ValueError(
            "Non zero coefficient is required to find the zero point."
        )

    result = []

    for i in range(degree - 1, -1, -1):
        result.append(xs[2 * i] / divisor)
        xs[2 * i] = 0
        divisor = xs[2 * i - 1]

    x = -xs[0] / divisor

    return x

