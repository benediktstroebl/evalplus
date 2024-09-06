import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    Returns sum of xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the polynomial equation poly(x) = 0.
    Only returns the first solution, even if there are multiple zeros.
    Works only for lists with an even number of coefficients, and the largest non-zero coefficient.
    """
    # Check if list has an even number of elements
    if len(coefficients) % 2 == 1:
        print("The list of coefficients must have an even number of elements")
        return None

    # Check if largest coefficient is positive
    if coefficients[-1] < 0:
        print("The largest coefficient must be non-negative")
        return None

    # Calculate the degree of the polynomial
    degree = len(coefficients) - 1

    # Create a list of coefficients with an extra zero
    padded_coefficients = [0] * (degree + 1) + coefficients

    # Iterate through possible x values
    for x in range(max(padded_coefficients) + 1):
        # Check if polynomial evaluates to 0 at x
        if poly(padded_coefficients, x) == 0:
            return x

    return None