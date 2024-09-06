import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns sum of coefficients[i] * x^i, for all i.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Returns only the first found zero.
    Works only with lists of even numbers of coefficients, with the largest coefficient non-zero.
    """
    # your code here, basically inverse of poly
    if len(coefficients) % 2 == 1 or coefficients[0] == 0:
        return None
    x = 0
    largest_coeff = max(coefficients)
    while abs(poly(coefficients, x)) > 1e-6:
        x += largest_coeff / (poly(coefficients, x) / largest_coeff)
        # return x,  
    return x