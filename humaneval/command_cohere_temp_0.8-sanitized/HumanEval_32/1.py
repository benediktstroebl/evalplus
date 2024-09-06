import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns sum of coefficients[i] * x**i, for i in range(len(coefficients)).
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for polynomial coefficients = coefficients such that f(x) = 0.
    Returns only one solution.
    Works only for lists of coefficients with even length, and
    largest non-zero coefficient.
    """
    largest_coeff = max(coefficients)
    if len(coefficients) % 2 == 1 or largest_coeff == 0:
        return "coefficients list must have even length, and contain a non-zero largest coefficient"
    # Solution:
    # We make another polynomial which evaluates to
    # polynomial[i] * (x-i)
    # Sum of these polys will be 0 when x = i
    # So if len(coefficients) is even, we take i = len(coefficients) // 2
    # If len(coefficients) is odd, we take i = (len(coefficients) // 2) - 1
    i = len(coefficients) // 2
    return poly(coefficients, i) == 0