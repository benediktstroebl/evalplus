import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Returns only the first found zero.
    Works only with lists of even numbers of coefficients,
    and skips lists with smallest coefficient equal to 0.
    """
    if len(coefficients) % 2 == 1 or coefficients[0] == 0:
        return None

    # assuming largest coefficient is not 0
    # if largest coefficient is 0, we could have 0 as solution
    # but we skip 0 coefficient earlier
    # so largest coefficient must be non zero
    x0 = -coefficients[-1] / coefficients[0]
    x1 = (len(coefficients) - 2) * x0
    return x1