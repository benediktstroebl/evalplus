import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Returns the value of x that makes the polynomial equal to zero, based on the coefficients.
    Only returns one solution, and works only with lists of even coefficients.
    """
    if len(coefficients) % 2 == 1:
        raise ValueError("List of coefficients must have an even number of elements")
    max_coefficient = max(coefficients)
    if max_coefficient == 0:
        raise ValueError("List of coefficients must contain at least one non-zero element")

    # Solution based on regression formula for a polynomial passing through the origin
    # https://en.wikipedia.org/wiki/Regression_line#Passing_through_the_origin
    x0 = -coefficients[0] / max_coefficient
    return x0