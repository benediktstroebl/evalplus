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
    # Check for empty list
    if len(xs) == 0:
        raise ValueError("List xs must not be empty")

    # Check for empty list of coefficients
    if len(xs) % 2 == 1:
        raise ValueError(
            "List xs must have even number of coefficients. Otherwise, find_zero will not work."
        )

    # find the coefficient with largest absolute value
    largest_abs_coeff = max(map(abs, xs))

    # find the coefficient with the same absolute value
    xs = list(map(lambda x: x / largest_abs_coeff, xs))

    # f(x) = a * x^2 + b * x + c
    a, b, c = xs[0], xs[1], xs[2]
    d = b ** 2 - 4 * a * c
    if d < 0:
        raise ValueError("There are no roots.")
    return (-b + math.sqrt(d)) / (2 * a)
