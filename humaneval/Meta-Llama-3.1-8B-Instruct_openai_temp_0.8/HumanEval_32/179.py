```python
import math
import numpy as np

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[2] * x^2 +.... xs[n] * x^n

    Args:
    xs (list): A list of coefficients of the polynomial.
    x (float): The point at which to evaluate the polynomial.

    Returns:
    float: The value of the polynomial at point x.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    Finds a zero point of a polynomial given its coefficients.

    Args:
    xs (list): A list of coefficients of the polynomial.
              It must have an even number of elements,
              with the largest non-zero coefficient first.

    Returns:
    float: A zero point of the polynomial.
    """
    # Check if the list has an even number of elements
    if len(xs) % 2!= 0:
        raise ValueError("xs must have an even number of elements")

    # Initialize the bracketing interval
    a = -1
    b = 1
    # Initialize the tolerance
    tol = 1e-5

    # Find a zero point using the bisection method
    while abs(b - a) > tol:
        c = (a + b) / 2
        # Evaluate the polynomial at c
        p_c = poly(xs, c)
        # Evaluate the polynomial at a
        p_a = poly(xs, a)
        # Evaluate the polynomial at b
        p_b = poly(xs, b)
        # If the polynomial does not change sign, we know a zero point is in the interval
        if p_c * p_a < 0:
            b = c
        else:
            a = c

    return (a + b) / 2
```

**Example usage:**

```python
# Example 1: f(x) = 1 + 2x
print(round(find_zero([1, 2]), 2))  # Output: -0.5

# Example 2: (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
print(round(find_zero([-6, 11, -6, 1]), 2))  # Output: 1.0
```