### Polynomial Evaluation and Zero Finding

```python
import math
import numpy as np

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    
    Args:
    xs (list): Coefficients of the polynomial in descending order of exponent.
    x (float): Point at which to evaluate the polynomial.
    
    Returns:
    float: Value of the polynomial at point x.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    Finds a zero point of a polynomial given its coefficients.
    
    Args:
    xs (list): Coefficients of the polynomial in descending order of exponent.
    
    Returns:
    float: A zero point of the polynomial.
    """
    if len(xs) % 2!= 0:
        raise ValueError("Only lists with an even number of coefficients are supported")
    
    while xs[-1] == 0 and len(xs) > 1:
        xs.pop()
    
    if len(xs) == 1:
        return -xs[0] / xs[1]
    
    # Use numpy's roots function to find all roots of the polynomial
    roots = np.roots(xs)
    
    # Return the first real root
    real_roots = [root.real for root in roots if root.imag == 0]
    return real_roots[0] if real_roots else None
```

### Example Usage

```python
print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

This script extends the original `find_zero` function to handle polynomials of any degree. It uses NumPy's `roots` function to find all roots of the polynomial and returns the first real root. If no real roots exist, it returns `None`. It also checks if the input list has an even number of coefficients and removes trailing zeros to ensure that a solution exists.