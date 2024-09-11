```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    Finds a zero of a polynomial with coefficients xs.

    xs are coefficients of a polynomial, with the largest non-zero coefficient as the constant term.
    This function finds a zero of the polynomial and returns it.
    The function only works for polynomials with an even number of coefficients.

    Parameters:
    xs (list): The coefficients of the polynomial, in ascending order of power.

    Returns:
    float: A zero of the polynomial.
    """
    # Ensure the polynomial has a positive constant term
    if xs[0] < 0:
        xs = [-coeff for coeff in xs]

    # Check if the polynomial has even number of coefficients
    if len(xs) % 2!= 0:
        raise ValueError("Polynomial must have an even number of coefficients")

    # Initialize the range for the binary search
    low = -1.0
    high = 1.0

    # Perform a binary search for a zero of the polynomial
    while high - low > 1e-6:
        mid = (low + high) / 2
        mid_value = sum([coeff * math.pow(mid, i) for i, coeff in enumerate(xs)])
        if math.isclose(mid_value, 0):
            return mid
        elif mid_value < 0:
            low = mid
        else:
            high = mid

    # If no zero is found, return the midpoint
    return (low + high) / 2


# Example usage
print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

This script includes the `poly` function for evaluating a polynomial at a given point and the `find_zero` function for finding a zero of a polynomial with even number of coefficients and positive constant term. The `find_zero` function uses a binary search algorithm to find a zero of the polynomial.