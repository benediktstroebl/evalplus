import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Returns only the first found zero, even if there are more.
    Works only for lists with even number of coefficients,
    and assumes the largest coefficient is not zero.
    """
    coeffs = [abs(c) for c in coefficients]
    div = coeffs[-2] / coeffs[-1]
    return -div