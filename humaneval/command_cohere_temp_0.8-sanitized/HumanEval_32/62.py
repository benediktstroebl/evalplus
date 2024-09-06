import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Returns only the first found zero, even if there are multiple.
    
    Precondition: len(coefficients) is even and coefficients[0] is nonzero, 
    ensuring that there is at least one solution.
    """
    # Check preconditions
    if len(coefficients) != 0 and coefficients[0] == 0:
        raise ValueError("Input coefficients list must have a non-zero leading coefficient.")
    if len(coefficients) % 2 == 1:
        raise ValueError("Input coefficients list must have an even length.")

    # Adapted from https://www.geeksforgeeks.org/find-all-zeroes-of-a-polynomial/
    x = -coefficients[0] / (coefficients[1:] + [0])
    return x