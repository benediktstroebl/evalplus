import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the polynomial equation poly(x) = 0.
    Only returns the first solution, if multiple solutions exist.
    Only works for lists of coefficients with an even number of items
    and the largest non-zero coefficient.
    """
    # Check if list has an even number of coefficients and a non-zero largest coefficient
    if len(coefficients) % 2 == 0 and coefficients[-1] != 0:
        # Calculate the polynomial value at the midpoint
        mid = (coefficients[-1] / 2)
        # If midpoint is a root, return it
        if poly(coefficients, mid) == 0:
            return mid
        # Calculate the polynomial value at x = mid + 1
        val = poly(coefficients, mid + 1)
        # If this value is 0, return x = mid + 1
        if val == 0:
            return mid + 1
        # Calculate the polynomial value at x = mid - 1
        val = poly(coefficients, mid - 1)
        # If this value is 0, return x = mid - 1
        if val == 0:
            return mid - 1
        # Calculate the rate of change of the polynomial value at x = mid
        rate = (poly(coefficients, mid + 1) - poly(coefficients, mid - 1)) / 2
        # Calculate the next potential root using the rate of change
        next_root = mid - rate
        # If the next potential root is within bounds, return it
        if next_root >= 0 and next_root <= 1:
            return next_root
    return None