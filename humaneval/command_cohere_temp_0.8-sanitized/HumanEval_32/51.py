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
        return None

    # flip sign to negative
    x = 10
    while True:
        # we have x^2 + ... x^n + 1 = 0
        # so x^n + ... + x^2 + 1 = 0
        # so (x^n + ... + x^2 + 1) / x = 0
        # so (x^n + ... + x^2 + 1) = -x
        # so x = - poly(x)
        if x == 0:
            return 0

        if abs(poly(coefficients, x)) < 1e-6:
            return x

        x = -x
        # prevent infinite loops
        if x == 10:
            return None