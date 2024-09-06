import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation polynomial == 0.
    Only returns the first solution founds, and only accepts lists of coefficients that have an even length
    and a largest non-zero coefficient, as these are sufficient and necessary conditions for there being a solution.
    
    Parameters:
        - coefficients: A list of floats representing the coefficients of a polynomial.

    Returns:
        A float representing the value of x at which the polynomial evaluates to zero.
    """
    if len(coefficients) % 2 == 1 or max(coefficients) == 0:
        return None

    # Sort coefficients descending by absolute value
    coefficients = sorted(coefficients, key=lambda x: abs(x), reverse=True)

    x_star = 0
    current_sum = coefficients[0]
    for coeff in coefficients[1:]:
        current_sum = current_sum * x_star + coeff
        x_star += 1 / current_sum

    return x_star