import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Returns only the first found zero, even if there are multiple.
    Works only for lists with even number of coefficients, and maximal coefficient != 0
    """
    n = len(coefficients)
    if n % 2 == 1 or coefficients[n // 2] == 0:
        return None

    # let y be the coefficient-less equation
    # y = x^n * poly(coefficients, x)
    # x = ????
    # => y = poly(coefficients, x)
    # => x = ???
    # => x^n = ??
    # x = ?? / n
    x0 = coefficients[n // 2] / n
    return x0