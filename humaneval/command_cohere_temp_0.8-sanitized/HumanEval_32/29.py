import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Returns only the first found zero, even if there are more.
    Works only for lists with even number of coefficients,
    and assumes the largest coefficient is not zero.
    """
    # Your code here, remove comments below to start.
    # Your code here should be a single expression yielding Float
    return (-coefficients[1] / (2 * coefficients[0])) ** (1 / 2)