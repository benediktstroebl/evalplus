import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Returns only the first found zero point.
    Works only with lists of even coefficients, assuming this is a polynomial with even degree.
    """
    if len(coefficients) % 2 == 1:
        raise ValueError("List of coefficients must have an even number of elements")
    max_coefficient = max(coefficients)
    if max_coefficient == 0:
        raise ValueError("List of coefficients must have at least one non-zero element")

    # Handle special cases of single term or constant polynomial
    if len(coefficients) == 2:
        return -coefficients[1] / coefficients[0]
    if len(coefficients) == 4 and coefficients[0] == 0 and coefficients[1] == 0:
        return -coefficients[2] / coefficients[3]

    x = -max_coefficient / (max_coefficient * max_coefficient - sum(coeff * coeff for coeff in coefficients[1:]))
    return x