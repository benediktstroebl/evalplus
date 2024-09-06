import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    Returns sum of terms xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Only returns the first solution, even if there are multiple zeros.
    Requires an even number of coefficients and the largest non-zero coefficient.
    """
    # Check for invalid inputs
    if len(coefficients) % 2 == 1 or coefficients[-1] == 0:
        raise ValueError("Input coefficients list must have an even length and a non-zero last coefficient.")

    # Handle special cases with constant polynomial
    if len(coefficients) == 2:
        return -coefficients[0] / coefficients[1]

    # Calculate shifts
    shift_n = -coefficients[len(coefficients) // 2] / coefficients[len(coefficients) // 2 - 1]
    shift_m = math.sqrt(shift_n * shift_n - 4 * coefficients[0] / coefficients[len(coefficients) // 2 - 1])
    x = (shift_m + shift_n) / 2

    # Verify solution
    if poly(coefficients, x) == 0:
        return x
    else:
        # If solution is outside bounds, reject it
        if x < -1 or x > 1:
            raise ValueError("Solution x is outside valid bounds (-1 <= x <= 1).")

        # If we reach this point, there is no solution
        raise ValueError("No valid solution exists for the provided polynomial.")