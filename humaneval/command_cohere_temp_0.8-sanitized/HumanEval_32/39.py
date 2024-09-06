import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns the value of the polynomial at x, given as sum(coeff * x^i for i, coeff in enumerate(coefficients)).
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation polynomial = 0.
    Returns only one solution, even if there are many.
    
    Moreover, this function only accepts lists coefficients 
    that have an even number of coefficients and the largest non-zero coefficient, 
    as it guarantees a solution.
    """
    if len(coefficients) % 2 == 1 or coefficients[-1] == 0:
        return None

    # invert the polynomial
    polynomial = [0] * len(coefficients)
    for i, coeff in enumerate(coefficients):
        polynomial[i] = -coeff

    x = poly(polynomial, 0)
    return -x