import math
import pytest
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns the result of summing each coefficient multiplied by the corresponding power of x.
    
    Parameters:
    coefficients (list): A list of floats representing the coefficients of the polynomial.
    x (float): The point at which to evaluate the polynomial.

    Returns:
    float: The result of evaluating the polynomial at the given point x.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.

    Parameters:
    coefficients (list): A list of floats representing the coefficients of a polynomial.

    Returns:
    float: A solution x for the equation poly(x) = 0. 
    """
    # Check for an even number of coefficients and a non-zero coefficient
    if len(coefficients) % 2 == 1 or coefficients[0] == 0:
        return None

    # Sort coefficients in descending order
    coefficients.sort(reverse=True)

    # Try to find a solution using the Remez algorithm
    def remez(x):
        return poly(x, coefficients)

    # Define boundaries for the Remez algorithm
    x_min = -10
    x_max = 10

    # Find approximation using Remez algorithm
    def approximation(degree):
        y_min = 1e12
        y_max = -1e12
        x_mid = (x_min + x_max) / 2

        for i in range(degree + 1):
            y_min, y_max = update_interval(y_min, y_max, i, x_mid, remez)
            x_mid = (y_min + y_max) / 2

        return x_mid

    # Update interval based on the sign of the function
    def update_interval(y_min, y_max, i, x_mid, remez):
        if i == 0:
            if remez(x_mid) > 0:
                y_min = 0
            else:
                y_max = 0
        else:
            if remez(x_mid) > 0:
                y_max = y_min
            else:
                y_min = y_max

        # Adjust boundaries based on the sign of the function
        if remez(x_mid) > 0:
            x_min = x_mid - 1
        else:
            x_max = x_mid + 1

        return y_min, y_max

    # Calculate the degree of the approximation
    degree = len(coefficients) // 2

    # Find solution using approximation
    solution = approximation(degree)

    # Check if solution is within boundaries
    if solution < x_min or solution > x_max:
        return None

    return solution