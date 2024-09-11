### Polynomial Evaluation and Zero Finder

Here's a Python script implementing the polynomial evaluation and zero finder as per the given problem statement:

```python
import math
import numpy as np

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.

    Args:
        xs (list): Coefficients of the polynomial.
        x (float): Point at which to evaluate the polynomial.

    Returns:
        float: Value of the polynomial at point x.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    Finds a zero point of a polynomial given its coefficients.

    Args:
        xs (list): Coefficients of the polynomial. The list must have an even number of elements.

    Returns:
        float: A zero point of the polynomial.
    """
    # Check if the list has an even number of elements
    if len(xs) % 2!= 0:
        raise ValueError("The list of coefficients must have an even number of elements.")

    # Initialize coefficients for the derived polynomial
    derived_xs = [0] * (len(xs) // 2)

    # Calculate coefficients of the derived polynomial
    for i in range(len(xs) // 2):
        derived_xs[i] = (xs[i*2+1] - xs[i*2+3]) / (i*2)

    # Find a zero point of the derived polynomial
    return -derived_xs[0] / (derived_xs[0]*2 + derived_xs[2])

# Example usage:
print(round(find_zero([1, 2]), 2)) # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2)) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

This script includes the `poly` function to evaluate a polynomial at a given point and the `find_zero` function to find a zero point of a polynomial given its coefficients. The `find_zero` function works by first deriving a new polynomial whose zeros are the zeros of the original polynomial and their negatives, and then finding the zero of this new polynomial.