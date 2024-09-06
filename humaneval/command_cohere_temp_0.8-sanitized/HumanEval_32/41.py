import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the polynomial equation xs[i] * x^i = 0.
    It returns only one solution, even if there are many.
    Additionally, it only accepts lists of coefficients xs
    that have an even length and the largest non-zero coefficient.
    """
    if len(coefficients) % 2 == 1 or coefficients[0] == 0:
        raise ValueError("List of coefficients must have an even length "
                         "and contain the largest non-zero coefficient.")

    x = 0
    largest_coeff = max(coefficients)

    for i in range(1, len(coefficients)):
        x = x - largest_coeff / (i + 1) * poly(coefficients, x)

    return x