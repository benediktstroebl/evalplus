import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns the value of the polynomial at x, given as sum(coeff * x^i for i, coeff in enumerate(coefficients)).
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Returns only the first found zero, even if there are multiple.
    Works only for lists with an even number of coefficients,
    and skips lists without a non-zero coefficient.
    """
    if len(coefficients) % 2 == 1 or not coefficients:
        return None

    # Calculates the derivative of the polynomial
    poly_der = [coeff * i for i, coeff in enumerate(coefficients)]

    # Starts searching for zero at a position slightly after the last coefficient
    x = coefficients[-1]
    while abs(poly(coefficients, x)) > 1e-6:
        # Increases or decreases the step size based on the sign of the polynomial
        if poly(coefficients, x) > 0:
            x -= 0.1
        else:
            x += 0.1

        # Checks if the polynomial is close to zero and evaluates the derivative at the current point
        if abs(poly(coefficients, x)) < 1e-6 and abs(poly_der[0]) < 1e-6:
            return x

    return None