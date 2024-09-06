import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns sum of terms: coefficients[0] + coefficients[1] * x + coefficients[2] * x^2 + ... + coefficients[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation: poly(x) = 0.
    Returns only one solution, even if there are many.
    Works only for lists with even numbers of coefficients, and with the largest non-zero coefficient.
    """
    if len(coefficients) % 2 == 1:
        raise ValueError("List of coefficients must have an even number of elements")
    if coefficients[-1] == 0:
        raise ValueError("List of coefficients must have a largest non-zero coefficient")

    # Divide coefficients into pairs of equal coefficients
    # i.e [a1, a2, a3, a4] => [([a1, a2], [a3, a4])
    pairs = zip(coefficients[:len(coefficients) // 2], coefficients[len(coefficients) // 2:])
    # Find angles for which tangent is equal to zero
    for pair in pairs:
        x_minus = poly(pair, -1) / poly(pair, +1)
        if abs(x_minus) < 1e-6:
            return math.sqrt(-x_minus)
    else:
        raise ValueError("Unable to find solution")