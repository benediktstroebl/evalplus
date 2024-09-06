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
    Returns only the first found zero, even if there are multiple zeros.
    
    Preconditions:
        - coefficients must be an even number of coefficients 
        - the largest non-zero coefficient must be positive (to be the highest order coefficient)
    """
    # Check preconditions
    if len(coefficients) % 2 == 1:
        raise ValueError('coefficients must have an even number of elements')
    if coefficients[-1] < 0:
        raise ValueError('the largest non-zero coefficient must be positive')
    
    # Define polynomial and target value
    polynomial = poly(coefficients, x=0)
    target = 0
    
    # Separate even and odd coefficients
    even_coeffs = [coeff for coeff in coefficients if coeff % 2 == 0]
    odd_coeffs = [coeff for coeff in coefficients if coeff % 2 != 0]
    
    # Iterate through potential roots
    for x in range(max(abs(odd_coeffs[0]), 1), 0, -1):
        # If polynomial evaluates to target at x
        if polynomial(x) == target:
            return x
        # If polynomial evaluates to target at x + 0.5
        if polynomial(x + 0.5) == target:
            return x + 0.5
    
    # If no root found, return last tried value
    return x