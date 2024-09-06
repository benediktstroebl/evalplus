import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Only returns the first solution found.
    
    Requires that the list of coefficients have an even number of elements 
    and the largest non-zero coefficient. 
    These conditions guarantee that there is exactly one solution.
    """
    if len(coefficients) % 2 == 1 or coefficients[-1] == 0:
        raise ValueError("List of coefficients must have an even number of elements and a non-zero largest coefficient.")
    x = -coefficients[-1] / (2 * coefficients[-2])
    return x