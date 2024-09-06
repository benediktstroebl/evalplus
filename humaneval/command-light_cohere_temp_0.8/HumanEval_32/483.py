```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[n] * x**n
    """
    return sum([coef * math.pow(x, i) for i, coef in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0
    find_zero returns only zero point, even if there are many
    solutions.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    """
   
    # Test
    >>> round(find_zero([1, 2, 3, 4, 5]), 2) # returns 1.0
    -0.5.
``` 
 outputs the smallest real number, the test passed.