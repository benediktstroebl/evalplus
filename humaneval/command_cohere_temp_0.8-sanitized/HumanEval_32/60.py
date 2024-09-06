import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns the result of summing each coefficient multiplied by the corresponding power of x.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation polynomial == 0.
    Only returns the first solution found, even if there are multiple zeros.

    Args:
        coefficients (list): Must contain an even number of coefficients, and the largest non-zero coefficient.

    Returns:
        float: A solution x for the equation polynomial == 0.
    """
    # Ensure that only valid input is provided
    if len(coefficients) % 2 == 1 or max(coefficients) == 0:
        raise ValueError("Input coefficients list must have an even length and contain a non-zero coefficient.")

    # Initialize guesses for the root and refinement threshold
    x_guess = -max(coefficients) / 2
    refinement_threshold = 0.0001

    # Iteratively refine the guess to find the zero
    while abs(poly(coefficients, x_guess)) > refinement_threshold:
        x_guess = (x_guess + x_guess) / 2

    return x_guess