import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation polynomial == 0.
    Returns only the first found zero point for the polynomial, even if there are multiple zeros.

    Args:
        coefficients (list): Must contain an even number of coefficients for a polynomial ax^2 + bx + c,
                            with the largest non-zero coefficient.

    Returns:
        float: A solution x for the polynomial equation.
    """
    a, b, c = coefficients[:3]
    root1, root2 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a), (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
    return min(root1, root2)