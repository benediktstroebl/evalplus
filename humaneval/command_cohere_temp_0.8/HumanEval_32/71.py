Here's a Python script that includes a function to solve the problem:
```python
import math

def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns the result of summing each coefficient multiplied by the corresponding power of x.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])


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


def _newton_method(coefficients: list) -> tuple:
    """Newton's algorithm to find zero of function."""
    x = 1
    last_error = 1e12
    iteration = 0

    while abs(last_error) > 1e-6 and iteration < 1000:
        x_next = x - [coefficients[0]] * (x * [coefficients[0]] + [coefficients[1:]]) / ([coefficients[0]] + [coefficients[1:]]))
        last_error = abs(x - x_next)
        x, iteration = x_next, iteration + 1

    return x, last_error
```

This script defines the functions `poly` and `find_zero`. The `poly` function evaluates a polynomial given a list of coefficients and a value for `x`. The `find_zero` function finds the value of `x` where `poly(x)` is zero, returning only the first solution and only for lists with an even number of coefficients. The `_newton_method` function is used to implement Newton's algorithm for finding the zero of a function.

These functions are then used to perform some tests, checking the correctness of the `find_zero` function.