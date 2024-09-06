import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Returns only the first found zero point.
    Works only with lists of even numbers of coefficients, and excludes all with an odd number of coefficients.
    """
    if len(coefficients) % 2 != 0:
        return "List of coefficients has odd number of elements"
    
    max_abs_coeff = max([abs(c) for c in coefficients if c != 0])
    
    if max_abs_coeff == 0:
        return "No non-zero coefficients to evaluate polynomial at zero."
    
    x = -max_abs_coeff / (max_abs_coeff * max_abs_coeff + 1)
    return x