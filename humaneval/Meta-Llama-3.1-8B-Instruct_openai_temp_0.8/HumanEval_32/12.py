### Polynomial Solver

Below is a Python script that uses the `numpy` library to solve the polynomial equation.

```python
import numpy as np

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    
    Args:
    xs (list): List of coefficients in ascending order of powers (e.g., [1, 2, 3] means 1 + 2x + 3x^2).
    x (float): Point at which to evaluate the polynomial.
    
    Returns:
    float: Value of the polynomial at point x.
    """
    return sum([coeff * np.power(x, i) for i, coeff in enumerate(reversed(xs))])


def find_zero(xs: list):
    """
    Finds a root of a polynomial with coefficients xs.
    
    Args:
    xs (list): List of coefficients in ascending order of powers (e.g., [1, 2, 3] means 1 + 2x + 3x^2).
    
    Returns:
    float: A root of the polynomial. If there are multiple roots, returns only one.
    """
    # Ensure xs has an even number of coefficients
    if len(xs) % 2!= 0:
        raise ValueError("xs must have an even number of coefficients")
    
    # Find the largest non-zero coefficient
    max_coeff = max(coeff for coeff in xs if coeff!= 0)
    
    # Initialize the interval [a, b] where [a, b] is the range where the root exists
    a = -10
    b = 10
    
    # Perform binary search to find a root
    while abs(a - b) > 1e-5:
        c = (a + b) / 2
        f_c = poly(xs, c)
        f_a = poly(xs, a)
        if f_c * f_a < 0:
            b = c
        else:
            a = c
    
    # Return a root
    return a

# Test cases
print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

This script uses the `numpy` library to efficiently compute powers of `x` in the polynomial evaluation. The `find_zero` function uses binary search to find a root of the polynomial, assuming that the root exists in the interval [-10, 10]. You may need to adjust this interval depending on the specific polynomial you are working with.