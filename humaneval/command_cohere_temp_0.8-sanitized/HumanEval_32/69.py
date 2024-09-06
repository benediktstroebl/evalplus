import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns the result of summing each coefficient multiplied by the corresponding power of x.
    
    Args:
        coefficients (list): A list of floats representing the coefficients of the polynomial.
        x (float): The point at which to evaluate the polynomial.

    Returns:
        float: The result of evaluating the polynomial at the given point x.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation polynomial == 0.
    Returns the value of x that makes the polynomial equal to zero, based on the given coefficients.
    
    Args:
        coefficients (list): A list of floats representing the coefficients of the polynomial.
    Returns:
        float: The value of x at which the polynomial equals zero.
    """
    if len(coefficients) % 2 == 1:
        # return an error message for an odd number of coefficients
        return "Error: Coefficients list must have an even number of elements."

    # sort coefficients in descending order
    coefficients.sort(key=lambda x: -x)

    # initialize guess
    x = 1

    while math.fabs(poly(coefficients, x)) > 1e-6:
        # update x
        x = x - poly(coefficients, x) / coefficients[0]

    return x