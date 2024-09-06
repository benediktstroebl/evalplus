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
    Works only with lists of even numbers of coefficients,
    and sets coefficients to [1, -coefficient_of_second_degree] correctly.
    """
    n = len(coefficients)
    if n % 2 == 1 or coefficients[0] < 0:
        raise ValueError("find_zero works with lists of even number of coefficients and sets coefficients to [1, -coefficient_of_second_degree] correctly. Found coefficients: {} of length: {}".format(coefficients, n))

    if n == 2:
        return -coefficients[1] / (2 * coefficients[0])

    # We make coefficients list into the form [1, -coefficient_of_second_degree]
    coefficients = [1, -coefficients[1]] + coefficients[2:]

    # Divide equation by the leading coefficient and set x equal to 0
    secondary_equation = poly(coefficients, 0) / coefficients[0]
    x = 0

    # Solve for the secondary equation
    while abs(secondary_equation) > 1e-6:
        x_prime = x - secondary_equation
        x = x_prime
        secondary_equation = poly(coefficients, x_prime) / coefficients[0]

    return x