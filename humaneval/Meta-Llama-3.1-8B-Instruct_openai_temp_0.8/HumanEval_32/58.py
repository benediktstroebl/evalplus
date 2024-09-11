**Polynomial Solver**
======================

Below is a Python script that uses numerical methods to find a root of a polynomial.

```python
import math
import numpy as np
from scipy.optimize import fsolve

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    Finds a root of the polynomial with coefficients xs.
    
    Parameters:
    xs (list): coefficients of the polynomial, largest non-zero coefficient first.
    
    Returns:
    float: a root of the polynomial, or None if no root is found.
    """
    # ensure the coefficients are in descending order
    xs = xs[::-1]
    
    # use numpy to convert the coefficients to a polynomial
    poly = np.poly1d(xs)
    
    # use fsolve to find a root of the polynomial
    try:
        root = fsolve(poly, 0)[0]
        return root
    except:
        return None

# Example usage:
print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x, root: -0.5
print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3, root: 1.0
```

This script uses the `fsolve` function from SciPy to find a root of the polynomial. It first converts the coefficients to a NumPy polynomial, then uses `fsolve` to find a root. 

**Note**: This script assumes that the coefficients are given in descending order, i.e., the largest non-zero coefficient is first. This is a requirement of the original `find_zero` function. 

Also, note that `fsolve` may not find an exact root, but rather an approximation. The accuracy of the result depends on the initial guess and the coefficients of the polynomial.