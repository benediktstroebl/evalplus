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
    Works only with lists of even numbers of coefficients, and skips coefficients with value 0.
    """
    # Check if list has an even number of coefficients
    if len(coefficients) % 2 == 1:
        raise ValueError("List of coefficients must have an even number of elements")
    # Sort coefficients by inverse magnitude, and remove zeros
    coefficients = [x for x in coefficients if x != 0]
    sorted_coefficients = sorted(coefficients, key=lambda x: -x)
    # Initialize candidates to be tested
    x_candidates = [0]
    # Calculate polynomial for each candidate, and pick new candidates
    # Based on roots of cubics sued https://en.wikipedia.org/wiki/Cubic_equation
    for i in range(1, len(sorted_coefficients)):
        x_candidates = [x for x in x_candidates if poly(sorted_coefficients[:i] + [0] + sorted_coefficients[i:], x) == 0]
    return x_candidates[0]