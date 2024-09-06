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
    if len(xs) % 2 != 0 or any(xs[i] for i in range(1, len(xs), 2)):
        raise Exception("Polynomial must have even number of coefficients and all must be non zero")

    # We can iterate only if all coefficients are non zero
    if any(xs[i] for i in range(1, len(xs), 2)):
        raise Exception("Polynomial must have all coefficients non zero")

    # Check if we have root
    if all(xs[i] for i in range(0, len(xs), 2)):
        return poly([0], 1)

    # calculate last term
    last_term = xs[-1] / xs[-2]

    # calculate x for zero
    x = 1 / last_term

    # calculate value of polynomial at x
    poly_x = poly(xs, x)

    # calculate the (x - x_zero) * (x - x_zero) ** (n / 2) term
    x_minus_x_zero = poly(xs, x - x) * poly(xs, x + x - x_zero)

    # calculate the (x - x_zero) * (x - x_zero) ** ((n + 1) / 2) term
    x_minus_x_zero_plus_one = poly(xs, x) * poly(xs, x - x_zero)

    # calculate the absolute value of the value at x
    x_minus_x_zero_plus_one_abs = abs(x_minus_x_zero_plus_one)

    # find x_zero
    if x_minus_x_zero_plus_one_abs < 0.5:
        return x + x_zero
    elif x_minus_x_zero_plus_one_abs < 0.9:
        return x - x_zero
    elif x_minus_x_zero_plus_one_abs < 1.1:
        return x_zero
    return x

