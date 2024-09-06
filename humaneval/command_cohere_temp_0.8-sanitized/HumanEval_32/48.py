import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns sum of coefficients[i] * x^i, for i equal to 0 to len(coefficients)-1.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the polynomial equation coefficients[i] * x^i = 0.
    Returns only one solution, even if there are many.
    Works only with lists of coefficients with even length and non-zero coefficients.
    """
    if len(coefficients) % 2 == 1 or not coefficients:
        raise ValueError("List of coefficients should have an even length and contain at least one non-zero coefficient.")

    # arrange coefficients in format [a, b, c, d, ...], where each coefficient is flipped sign.
    flipped = [-coef for coef in coefficients]
    flipped.append(0)
    
    # Calculate polynomial value for x = -coefficients[0] / (coefficients[1:] + flipped[:-1])
    x = -coef_div(coefficients[0], coefficients[1:] + flipped[:-1])
    
    # Check if result is zero
    if abs(poly(coefficients, x)) < 1e-6:
        return x
    else:
        # If not, something went wrong, return NaN
        return math.nan
def coef_div(a: float, b: list) -> float:
    """
    Utility function to divide a coefficient a by the list of coefficients b.
    Returns float - sum(b[i] / a) / (len(b) - 1)
    """
    return -sum(b[i] / a for i in range(len(b))) / (len(b) - 1)