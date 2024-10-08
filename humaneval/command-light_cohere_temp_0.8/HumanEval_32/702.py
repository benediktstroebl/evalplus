```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs.sum([coeff *0] + xs[1] * x + xs[1] * x**2 + .... xs[n] * x**n)
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero finds x that makes polynomial equal to 0.
    find_zero returns only zero point, even if there are many
    solutions.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0

def test():
    """
    This function contains tests for the polynomial and find_zero functions.
    Test if polynomial is evaluated with coefficients (2,3,4,5) and x = 1. Test if polynomial
    test is performed with coefficients (1,2,3,4,5) and x = 2. Test if polynomial is find_zero with coefficients [1,2,3,4,5] and x = 1.0.
    test values: assert (poly(xs,x) == 20), "Test failed"
    test

xs = [1,2,3,4,5]
xs = [1,2,3,4,5]
xs = [1,2,3,4,5,6,7]
xs = [1,2,3,4,5,6,7,8]

print("Test passed")
```