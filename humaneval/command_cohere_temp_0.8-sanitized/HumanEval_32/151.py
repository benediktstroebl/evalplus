import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns the result of summing each coefficient multiplied by the corresponding power of x.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Returns only the first found zero point.
    Works only with lists of even numbers of coefficients, and excludes all with an odd number of coefficients.
    """
    if len(coefficients) % 2 != 0:
        return "List of coefficients has odd number of elements"
    max_abs_coeff = max([abs(coeff) for coeff in coefficients if coeff != 0])
    if max_abs_coeff == 0:
        return "No solution, because list has only zeros"
    return poly(coefficients, -1 / max_abs_coeff)