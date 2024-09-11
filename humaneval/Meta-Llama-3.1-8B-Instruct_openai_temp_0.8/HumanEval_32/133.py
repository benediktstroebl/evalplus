```python
import math
import numpy as np

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    Finds x such that poly(x) = 0.
    Returns only one zero point, even if there are many.
    Assumes xs are coefficients of a polynomial with an even number of coefficients,
    and the largest non-zero coefficient is at the end (guarantees a solution).
    """
    # Ensure xs has an even number of coefficients
    if len(xs) % 2!= 0:
        raise ValueError("xs must have an even number of coefficients")
    
    # Initialize coefficients for the derivative of the polynomial
    xs_derivative = [0] * len(xs)
    
    # Compute the coefficients for the derivative
    for i in range(len(xs) - 1):
        xs_derivative[i] = (i + 1) * xs[i + 1]
    
    # Find the root of the derivative, which is a zero of the original polynomial
    # We use a numerical method (bisection) to find the root
    a = -1
    b = 1
    while abs(b - a) > 1e-6:
        c = (a + b) / 2
        if poly(xs_derivative, c) * poly(xs_derivative, a) < 0:
            b = c
        else:
            a = c
    
    # Evaluate the polynomial at the root of the derivative to ensure it is a zero
    # If the polynomial is not exactly zero, raise a warning
    if abs(poly(xs, (a + b) / 2)) > 1e-6:
        import warnings
        warnings.warn(f"The polynomial {poly(xs, (a + b) / 2)} is not exactly zero at x = {(a + b) / 2}.")
    
    return (a + b) / 2

# Example usage:
print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```