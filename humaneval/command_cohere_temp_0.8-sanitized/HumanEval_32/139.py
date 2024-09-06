import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns sum of coefficients[i] * x^i, for i = 0 to n-1
    where n = len(coefficients).
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Returns only the first found zero.
    Works only for lists with even number of coefficients,
    and skips lists with smallest coefficient equal to 0.
    """
    if len(coefficients) % 2 == 1 or coefficients[0] == 0:
        return None

    # rotate list, moving largest coefficient to first position
    coefficients = coefficients[1:] + [coefficients[0]]

    # divide in two lists, in rotation
    mid = len(coefficients) // 2
    left = coefficients[:mid]
    right = coefficients[mid:]

    # in alternating fashion, try solving polynomial with
    # coefficients on the left, then on the right
    x_left = find_zero_helper(left)
    if x_left is not None:
        return x_left
    else:
        return find_zero_helper(right)
def find_zero_helper(coefficients: list) -> float:
    """
    Tries to solve polynomial equation with given coefficients.
    Wrapper to deal with edge case of find_zero being called
    with list with one element, and to avoid repeated coefficient checks.
    """
    if len(coefficients) == 1:
        return 0 if coefficients[0] == 0 else 1 / coefficients[0]

    x_lower = -10
    x_upper = 10
    while x_upper - x_lower > 1e-5:
        x_mid = (x_upper + x_lower) / 2
        if poly(coefficients, x_mid) == 0:
            x_lower = x_mid
        else:
            x_upper = x_mid
    return x_lower