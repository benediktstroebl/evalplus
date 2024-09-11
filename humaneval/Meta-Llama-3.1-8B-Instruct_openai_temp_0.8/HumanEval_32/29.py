```python
import math
import cmath
import numpy as np

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n
    """
    return sum([coeff * (x ** i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    Finds a zero of a polynomial with coefficients xs.
    It uses numpy's roots function to find all zeros and then returns the closest one to the origin.
    """
    if len(xs) % 2!= 0:
        raise ValueError("Polynomial must have an even number of coefficients.")
    
    # Reverse coefficients to make numpy's poly1d function work correctly
    xs-reversed(xs)
    
    # Find all roots of the polynomial
    roots = np.roots(xs)
    
    # Return the root with the smallest absolute value (i.e., closest to the origin)
    return min(roots, key=abs)

# Test cases
print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

This script defines the `poly` function to evaluate a polynomial at a given point, and the `find_zero` function to find a zero of a polynomial. The `find_zero` function now uses numpy's `roots` function to find all zeros of the polynomial and returns the one closest to the origin. 

Note that this script implicitly uses the `numpy` library for its `roots` function, which is used to find the zeros of the polynomial. If you don't have numpy installed, you can do so with pip:

```bash
pip install numpy
```