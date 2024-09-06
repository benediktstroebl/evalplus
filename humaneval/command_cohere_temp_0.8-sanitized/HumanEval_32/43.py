import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns the result of summing each coefficient multiplied by the corresponding power of x.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Returns the value of x that makes the polynomial equal to zero, based on the coefficients.
    Requires an even number of coefficients and assumes the largest non-zero coefficient is the dominant term.
    """
    if len(coefficients) % 2 == 1:
        raise ValueError("List coefficients must have an even number of elements")
    if coefficients[-1] == 0:
        raise ValueError("Last coefficient must be non-zero")

    # Create a copy of coefficients with negative coefficient
    xs = [-coeff for coeff in coefficients]
    x = -xs[-1] / (2 * xs[0])
    # Check if close to zero
    if abs(x) < 1e-6:
        return 0
    while True:
        if poly(xs, x) == 0:
            return x
        # Calculate next guess
        x_prev = x
        x = (x + x_prev) / 2
    return None