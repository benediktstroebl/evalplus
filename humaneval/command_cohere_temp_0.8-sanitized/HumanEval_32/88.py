import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution for the equation poly(x) = 0.

    Args:
        coefficients (list): A list of floats representing the coefficients of the polynomial.

    Returns:
        float: A solution for the equation poly(x) = 0. 
    """
    # Check for an empty or an odd list of coefficients
    if len(coefficients) == 0 or len(coefficients) % 2 == 1:
        raise ValueError("List of coefficients should be of even length")

    # Sort coefficients in descending order
    coefficients.sort(reverse=True)

    # Number of terms in the polynomial
    n = len(coefficients)

    # Calculate the discriminant
    discriminant = 4 * n * coefficients[0]

    # Initialize roots with large values
    roots = [float("inf")] * n

    # Calculate the roots
    for i in range(n):
        root_power = n - i - 1
        roots[i] = (-1) ** i * math.sqrt(discriminant / coefficients[i])

    # Filter out the extraneous roots
    # Only one root is returned, if exists
    for root in roots:
        if root != float("inf"):
            return root