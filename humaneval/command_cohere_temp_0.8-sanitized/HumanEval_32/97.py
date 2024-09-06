import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for polynomial polynomial eqaution poly(x) = 0.
    Returns only one solution x, even if there are more than one.
    Also, it only works with lists coefficients having even length
    and assumes coefficient with largest absolute value is the leading coefficient.
    """
    leading_coefficient = max(coefficients)
    xs = [float(-leading_coefficient) / float(leading_coefficient) for i in range(1, len(coefficients) // 2 + 1)]
    x = 1
    for power in range(1, len(xs)):
        x = x * xs[power]
    return x