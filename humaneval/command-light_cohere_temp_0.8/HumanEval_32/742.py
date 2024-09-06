```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[-1] * x**(-1)
    """
    return sum([coefficient * math.pow(x, i) for i, coefficient in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero finds x such that poly(x) = 0
    find_zero returns x only if there is exactly one solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
   
   
    """
    > round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    -0.5)
```
poly([1, 2])
poly( [1, -4, 2, -3])
find_zero([1, -4, 2, -3])
```
The script defines a function `poly` that evaluates a polynomial at a given point `x`. The `find_zero` function finds the roots of the polynomial and returns only the root(s) with the largest non-zero coefficient.  The root finding is done by finding the zero of the polynomial.