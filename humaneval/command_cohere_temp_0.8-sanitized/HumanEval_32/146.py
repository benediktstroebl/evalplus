import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns sum of coefficients[i] * x^i, for i = 0 to len(coefficients) - 1.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Returns only the first found zero.
    Works only with lists of even numbers of coefficients,
    and where the largest coefficient is non-zero.
    """
    if len(coefficients) % 2 == 1 or coefficients[0] == 0:
        return None

    # revolve all coefficients to positive
    coefficients = [abs(coeff) for coeff in coefficients]
    max_coefficient = max(coefficients)
    coefficients = [coeff / max_coefficient for coeff in coefficients]
    solution = find_zero_raw(coefficients, max_coefficient)
    return solution * max_coefficient
def find_zero_raw(coefficients: list, denominator: float) -> float:
    """
    Private function that finds zero using nominal coefficients.
    Will return None if denominator == 0.
    """
    x = denominator
    prev = float("inf")
    while abs(poly(coefficients, x)) > 1e-6:
        prev = x
        x -= poly(coefficients, x) / denominator
    if abs(x - prev) < 1e-6:
        return None
    return x