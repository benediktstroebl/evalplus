import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    Returns sum of terms xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Returns only one solution, even if there are many.
    Works only with lists of coefficients with even length and the largest non-zero coefficient.
    """
    if len(coefficients) % 2 == 1 or coefficients[0] == 0:
        return None

    # rearrange coefficients in descending order and flip sign
    coefficients = [abs(c) for c in coefficients[::-1]]
    polynomial = poly(coefficients, x=x)
    x = 0

    while polynomial > 0: 
        x -= 1 
        polynomial //= 2 
    return x