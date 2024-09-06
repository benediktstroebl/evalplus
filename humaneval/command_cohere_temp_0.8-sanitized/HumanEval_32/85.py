import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns sum of coefficients[i] * x^i, for i = 0 to len(coefficients) - 1.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation polynomial = 0.
    Returns only the first found zero.
    Works only with lists of even numbers of coefficients,
    and skips lists with smallest coefficient == 0.
    """
    if len(coefficients) % 2 == 1 or coefficients[0] == 0:
        return None

    # skip even coefficients
    coefficients = [val for val in coefficients if val != 0]

    x = -coefficients[0] / (coefficients[1:] + [0.0])
    y = poly(coefficients, x)
    if abs(y) < 1e-5:  # exit early if close to zero
        return x

    # converge from both sides
    left_bound, right_bound = -10, 10
    while left_bound < right_bound:
        x = (left_bound + right_bound) / 2
        y = poly(coefficients, x)
        if abs(y) < 1e-5:
            return x
        elif y > 0:
            right_bound = x
        else:
            left_bound = x + 1

    return None