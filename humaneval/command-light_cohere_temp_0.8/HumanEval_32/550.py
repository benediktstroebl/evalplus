```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + .... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero finds x that makes polynomial equal to zero
    find_zero returns x and checks it doesn't equal to any negative infinity.

    find_zero finds only zero point, even if there are many solutions. It ensures that all solutions are valid solutions, and returns only one solution.

    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    """
   
    test: assert find_zero([1, 2]) == (-0.5), pass
    verifications
   
    test: assert find_zero([-6, 11, -6, 1]) == (-1.0, -2.5); pass
    test: assert find_zero([-3, 4, -5, 2, -3]) == (-3.5, -5.0); pass verifications
   
```