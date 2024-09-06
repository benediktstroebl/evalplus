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
    Works only with lists of even numbers of coefficients, with the largest coefficient non-zero.
    """
    if len(coefficients) % 2 == 1 or coefficients[0] == 0:
        return "Coefficients list must have an even number of elements and the largest coefficient cannot be zero."

    max_abs_coeff = max(coefficients, key=abs)
    x = -max_abs_coeff / (2 * poly(coefficients, max_abs_coeff / (2)))
    return x