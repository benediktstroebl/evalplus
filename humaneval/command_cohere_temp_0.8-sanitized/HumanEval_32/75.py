import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns the value of the polynomial at x, given as:
        coefficients[0] + coefficients[1] * x + coefficients[2] * x^2 + ... + coefficients[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Returns only the first found zero, even if there are multiple zeros.
    
    Additionally, this function only accepts lists of coefficients that have an even length 
    and the list must not contain zeros (except for the last element, which can be zero).
    It guarantees a solution if these conditions are met.
    
    """
    # Ensure proper formatting:
    if len(coefficients) % 2 == 1 or any(coeff for coeff in coefficients if coeff == 0):
        raise ValueError("Input list of coefficients must have an even length and no zero elements apart from the last one.")

    # Inverse power iteration to find a zero of the polynomial:
    x = 1.0
    while abs(poly(coefficients, x)) > 1e-6:
        x *= -1
    return x