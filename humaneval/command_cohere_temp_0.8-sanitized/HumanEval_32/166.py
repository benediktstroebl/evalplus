import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Returns only the first found zero, even if there are multiple.

    Preconditions:
        - coefficients list must be of even length
        - must have at least one non-zero coefficient (all coefficients can be zero, but this is not useful)
    """
    # your code here

    # Filter out leading zeros
    non_zero_index = next(i for i, coeff in enumerate(coefficients) if coeff)
    trimmed_coefficients = coefficients[non_zero_index:]

    # Handle special cases of linear and quadratic polynomials
    if len(trimmed_coefficients) == 1:
        return -trimmed_coefficients[0] / 2.0
    elif len(trimmed_coefficients) == 2:
        return -trimmed_coefficients[1] / (2.0 * trimmed_coefficients[0])

    # Divide by leading coefficient and flip sign to negate the equation
    x = -trimmed_coefficients[0] / 2.0
    for i in range(len(trimmed_coefficients)):
        x = x - trimmed_coefficients[i] / (2.0 * math.pow(x, i + 2))

    return x