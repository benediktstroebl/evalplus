### Evaluates and Finds Zero of a Polynomial

```python
import math
import numpy as np

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    
    Args:
    xs (list): coefficients of the polynomial
    x (float): point at which to evaluate the polynomial
    
    Returns:
    float: value of the polynomial at x
    
    Example:
    >>> poly([1, 2], 2) # f(x) = 1 + 2x
    5.0
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    Finds a zero point of a polynomial.
    
    Args:
    xs (list): coefficients of the polynomial
    
    Returns:
    float: a zero point of the polynomial
    
    Raises:
    ValueError: if the polynomial has an odd number of coefficients or no non-zero coefficients
    
    Example:
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    if len(xs) % 2!= 0:
        raise ValueError("Polynomial must have an even number of coefficients")
    
    # Find the largest non-zero coefficient
    largest_coeff = max(coeff for coeff in xs if coeff!= 0)
    
    # The zero point should be in the range [0, 2] for efficiency
    for x in np.linspace(0, 2, 1000):
        if abs(poly(xs, x)) < 1e-6:
            return x
    
    raise ValueError("No zero point found")

# Example usage:
print(round(find_zero([1, 2]), 2)) # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2)) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

This script uses the `numpy` library to perform efficiently. The `find_zero` function attempts to find a zero point by evaluating the polynomial at multiple points in the range [0, 2] and returning the first point that gives a value close to 0. If no zero point is found, it raises a `ValueError`.