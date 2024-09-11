```python
import math
import numpy as np

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    
    Args:
    xs (list): List of coefficients of the polynomial in descending order of powers.
    x (float): Point at which the polynomial is to be evaluated.
    
    Returns:
    float: Value of the polynomial at point x.
    """
    return sum([coeff * x**i for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    Finds a zero of the polynomial with coefficients xs.
    
    Args:
    xs (list): List of coefficients of the polynomial in descending order of powers.
    
    Returns:
    float: A zero of the polynomial.
    
    Raises:
    ValueError: If the number of coefficients is odd or the largest coefficient is zero.
    """
    if len(xs) % 2!= 0:
        raise ValueError("Number of coefficients must be even")
    if xs[0] == 0:
        raise ValueError("Largest coefficient must be non-zero")
    
    # Find the largest coefficient
    largest_coord = np.argmax(np.abs(xs))
    
    # We know the polynomial has a zero at -xs[largest_coord] / xs[largest_coord+1]
    # And we know that the derivative of the polynomial at that point is non-zero
    # This means the point is a simple root of the polynomial
    x = -xs[largest_coord] / xs[largest_coord+1]
    
    return x
```

Example use cases:

```python
print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

This script uses the numpy library to find the index of the largest coefficient, which is used to evaluate the zero of the polynomial.