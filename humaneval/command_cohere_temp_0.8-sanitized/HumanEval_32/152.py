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
    Returns only the first found zero solution, even if there are more.
    Works only for lists with an even number of coefficients,
    and assumes the largest coefficient is not zero as it guarantees
    a solution.
    """
    if len(coefficients) % 2 == 1 or max(coefficients) == 0:
        return "Invalid input for find_zero()"

    # invert the polynomial
    polynomial = [0] * len(coefficients)
    for i in range(len(coefficients)):
        polynomial[i] = -coefficients[i]

    x = 0
    last_val = poly(polynomial, x)
    while not abs(last_val) < 1e-5:
        # invert the last value
        last_val_inv = 1 / last_val
        # update x
        x += last_val_inv
        # evaluate the polynomial at the new location
        last_val = poly(polynomial, x)
    return x