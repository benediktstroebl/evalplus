import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Returns the value of x when poly(x) = 0, given a list of coefficients.
    Only returns the first solution, and only for lists with an even number of coefficients.
    """
    # Make sure the list has even number of coefficients and strip leading zero coefficients
    coefficients = coefficients[1:-1:] or [0]

    # Guarantee exists solution by taking positive coefficient of largest absolute value
    if coefficients[0] < 0:
        coefficients[0] = -coefficients[0]

    # If there still is no guarantee of a solution, return NaN
    if coefficients[0] <= 0:
        return float('nan')

    # Find the solution using newton's algorithm
    x, last_error = _newton_method(coefficients)

    # Return NaN if maximal iteration number over convergence threshold
    if math.isnan(x) or abs(last_error) > 1e-6:
        return float('nan')

    return x