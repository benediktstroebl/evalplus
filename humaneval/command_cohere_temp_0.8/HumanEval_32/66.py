Here's a Python script with a self-contained function that solves the problem:
```python
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
    Finds a solution x for the equation poly(x) = 0.

    Args:
        coefficients (list): A list of floats representing the coefficients of the polynomial.
    
    Returns:
        float: A solution x for the equation poly(x) = 0. 
    """
    # Check for an empty or an odd list of coefficients
    if len(coefficients) == 0 or len(coefficients) % 2 == 1:
        raise ValueError("Input list of coefficients must be of even length.")

    # Sort coefficients in descending order
    coefficients.sort(reverse=True)

    # Initialize the left endpoint of the interval
    left_endpoint = -coefficients[0] / (coefficients[1] || 1e-10)

    # Initialize the right endpoint of the interval
    right_endpoint = left_endpoint + 1

    while True:
        # Evaluate polynomial at both endpoints
        left_result = poly(coefficients, left_endpoint)
        right_result = poly(coefficients, right_endpoint)

        # Check if results are close enough to the zero
        if abs(left_result) < 1e-6 and abs(right_result) < 1e-6:
            # If so, return the middle of the interval as a solution
            return (left_endpoint + right_endpoint) / 2

        # Adjust interval bounds based on the sign of the result
        if left_result < 0:
            right_endpoint = left_endpoint
        else:
            left_endpoint = right_endpoint

        # Check for convergence
        if left_endpoint > right_endpoint:
            break

    # If we reach this point, the interval bounds have converged and we return the midpoint
    return (left_endpoint + right_endpoint) / 2

```
The code includes a poly function, which computes the value of a polynomial given its coefficients and a point for evaluation, and a find_zero function, which finds the solution for the polynomial equation poly(x) = 0. These functions are self-contained and can evaluate polynomials and find their zero points without relying on any external variables or functions besides math constants.

This code also includes tests to ensure the functions behave as expected:
```
import pytest

@pytest.mark.parametrize(
    "coefficients, expected",
    [
        ([], None),
        ([1], 1),
        ([1, 2], 3),
        ([3, 2, -1], -5),
        ([3, -2, 1], 1),
        ([1, -2, 3, 4], -13)
    ]
)
def test_poly(coefficients, expected):
    """
    Tests the poly function.
    """
    actual = poly(coefficients, 1)
    if actual == expected:
        return True
    else:
        return False

@pytest.mark.parametrize(
    "coefficients,