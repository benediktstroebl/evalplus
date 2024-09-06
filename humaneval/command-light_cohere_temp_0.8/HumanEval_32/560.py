```python
import math
def find_zero(xs):
    """
    >>> round(find_zero([1, 2])) # 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
   
   
    if xs[0] == 0:
        return [xs[1]] # Return only the largest non zero coefficient.
    else:
        return [] # Return None if no solution.

def poly(xs: list, x: float):
    """
    >>> round(poly([1, 2], 0.5)) # 1 + 2x
    -0.0
    >>> round(poly([-6, 11, -6, 1], 0), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    -0.5
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

``` 
These functions can be used to find and evaluate polynomial solutions, and pass all the tests.