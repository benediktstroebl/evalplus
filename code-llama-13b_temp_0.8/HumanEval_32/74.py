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

    # Check xs is of even length
    if len(xs) % 2 != 0:
        return "Error: xs should be of even length"

    # Check all coefficients in xs are 0 except the largest non zero coefficient
    for i, coeff in enumerate(xs):
        if i == 0:
            continue
        if coeff != 0:
            return "Error: All coefficients in xs should be 0 except the largest non zero coefficient"

    # Check non zero coefficients are positive
    if xs[0] < 0:
        return "Error: All coefficients in xs should be positive"

    # Calculate x_0
    x_0 = -1 * xs[1] / (2 * xs[0])

    # Calculate x_1
    x_1 = math.pow(x_0, 2) - xs[2] / xs[0]

    # Check if x_1 is positive
    if x_1 < 0:
        return "Error: x_1 is not positive"

    # Calculate x_1 by taking the positive root
    x_1 = math.sqrt(x_1)

    # Calculate x_2 = x_0 - x_1 and x_3 = x_0 + x_1
    x_2 = x_0 - x_1
    x_3 = x_0 + x_1

    # Check if either of x_2 or x_3 is zero
    if x_2 == 0:
        return x_3
    if x_3 == 0:
        return x_2

    # Return the zero point closest to origin
    if abs(x_2) < abs(x_3):
        return x_2
    return x_3

