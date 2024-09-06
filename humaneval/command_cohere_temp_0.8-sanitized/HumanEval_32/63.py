import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns sum of coefficients[i] * x^i, for i = 0 to n-1
    where n = len(coefficients).
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Returns only the first found zero, even if there are multiple.
    Guarantees a solution only for lists of coefficients with an even count
    and the largest non-zero coefficient.
    """
    # Ensure sufficient length and non-zero largest coefficient
    if len(coefficients) % 2 == 1 or coefficients[0] == 0:
        return None

    # Factors of the largest coefficient
    factors = [factor for factor in range(1, int(math.sqrt(coefficients[0])) + 1) if coefficients[0] % factor == 0]
    
    # Potential solutions
    solutions = [x for x in factors if poly(coefficients, x) == 0]
    
    # Returning the first solution
    return solutions[0] if solutions else None