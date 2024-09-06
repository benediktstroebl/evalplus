import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns the value of the polynomial at x, given as follows:
    coefficients[0] + coefficients[1] * x + coefficients[2] * x^2 + ... + coefficients[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Returns only the first found zero, even if there are multiple.
    
    Additionally, this function only accepts lists of coefficients 
    that contain an even number of coefficients and have the largest non-zero coefficient.
    
    This is because the rational root test (https://en.wikipedia.org/wiki/Rational_root_theorem) 
    guarantees a solution.
    """
    if len(coefficients) % 2 == 1 or coefficients[0] == 0:
        return None

    largest_coeff = max(coefficients)
    root = math.sqrt(largest_coeff)
    x = -root
    while abs(x) <= root:
        if poly(coefficients, x) == 0:
            return x
        x += 1 if x != -root else -1
        if abs(x) > root:
            return None
    return None