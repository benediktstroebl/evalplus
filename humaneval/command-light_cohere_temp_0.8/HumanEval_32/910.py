```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs.sum([coeff *i * x** for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero finds x that makes poly(x) = 0
    find_zero returns only zero point, even if there are many.
    => round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5

    
    
    @Test Case:
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    """
    """
    Test case using a polynomial with even number of coefficients.
    """
```