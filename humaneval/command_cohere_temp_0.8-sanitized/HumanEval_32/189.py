import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns the result of summing each coefficient multiplied by the corresponding power of x.
    
    Parameters:
        - coefficients: A list of floats representing the polynomial coefficients in order of powers.
        - x: The point at which to evaluate the polynomial.

    Returns:
        The result of evaluating the polynomial at x.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation coefficients[i] * x^i = 0.
    Returns the value of x that makes the polynomial equal to zero.
    
    Parameters:
        - coefficients: A list of floats representing the polynomial coefficients in order of powers.

    Returns:
        A float representing the value of x that solves the equation.
    """
    if len(coefficients) % 2 == 1 or max(coefficients) == 0:
        return "The list of coefficients should have an even number of elements and define a polynomial with a known root for the find_zero function to work correctly."

    x_values = [x / max(coefficients) for x in range(len(coefficients) + 1)]
    polynomial_values = [poly(coefficients, x) for x in x_values]

    # Exploit the fact that the polynomial has an even number of coefficients and therefore must have a root.
    # The root occurs exactly at the boundary between two consecutive x values, hence the floor division.
    return x_values[polynomial_values.index(min(polynomial_values))]