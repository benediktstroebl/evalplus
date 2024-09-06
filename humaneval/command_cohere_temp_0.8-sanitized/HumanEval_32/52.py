import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns the value of the polynomial at x, given as follows:
        coefficients[0] + coefficients[1] * x + coefficients[2] * x^2 + ... + coefficients[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Returns only the first found zero, even if there are multiple.
    Guarantees a solution only for lists of coefficients with an even number of items,
    and having the largest non-zero coefficient.
    """
    if len(coefficients) % 2 == 1 or coefficients[0] == 0:
        return None

    # calculate polynomial value at x = 0
    initial_value = poly(coefficients, 0)

    # if initial_value is zero, every polynomial evaluation is zero
    if initial_value == 0:
        return 0

    # iterate over decreasing x values and evaluate polynomial
    for x in range(1, 1001):
        eval_value = poly(coefficients, x)
        if eval_value == 0:
            return x

    return None