```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs.sum([coeff *for i, j, k) <= len(xs) for i,j,k in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero finds x such that poly(x) = 0.
    find_zero returns only zero point, even if there are many solutions
    and always returns the same value.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    """
   
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.2
   
   
   
    >>> round(find_zero([4, -5, 3, 4, 4, 5, 3]), 2) # (x + 4) * (x + 3) * 2 = 4 + 13x^2
    -3 + 8x + 4x^2 + 5x^3
    1.0
   
   
   
    ```