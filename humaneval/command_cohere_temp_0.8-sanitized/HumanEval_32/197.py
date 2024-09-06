import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns sum of coefficients[i] * x^i, for i equal to 0..n
    where n = len(coefficients)
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Returns only the first found zero, even if there are multiple.
    Works only for lists with even number of coefficients,
    and assigns zero to return value if input list lacks even number of coefficients.
    """
    if len(coefficients) % 2 == 1:
        return 0.0  # Return 0 if odd number of coefficients, as no valid polynomial exists.
    max_pow = len(coefficients) // 2
    x = float(-max_pow)
    while poly(coefficients, x) == 0:
        x = x + 1.0
    return x