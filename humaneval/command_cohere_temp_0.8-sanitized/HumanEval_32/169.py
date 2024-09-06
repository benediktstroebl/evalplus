import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns sum of terms: coefficients[0] + coefficients[1] * x + coefficients[1] * x^2 + ... + coefficients[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation: poly(x) = 0.
    Returns only one solution, even if there are many.
    Works only with lists of even numbers of coefficients,
    and with the largest non-zero coefficient set to 1.
    """
    if len(coefficients) % 2 == 1:
        raise ValueError('List of coefficients must have an even number of elements')
    max_idx = len(coefficients) - 1
    if coefficients[max_idx] == 0:
        raise ValueError('List of coefficients must have the largest non-zero coefficient set to 1')

    # Check that equation has a solution
    max_coefficient = coefficients[max_idx]
    tmp_coefficients = [max_coefficient] * len(coefficients)
    for i, coeff in enumerate(coefficients):
        tmp_coefficients[i] = coeff / max_coefficient

    tmp_poly = lambda x: poly(tmp_coefficients, x)
    x0 = 0
    x1 = 1
    while x1 - x0 > 1e-6:
        x2 = (x0 + x1) / 2
        if tmp_poly(x2) < 0:
            x1 = x2
        else:
            x0 = x2
    return x0