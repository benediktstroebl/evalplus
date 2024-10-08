```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero find x such that polynomial (x - x0) has 0 as its coefficient at ith index.
    find_zero returns only zero point, even if there are many solutions
    and returns a tuple (x0, x).

    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
   
   
    #  (x0, x) = (-1, 1)
    -0.4
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    -0.6
    #  (x0, x) = (-1, 1.0)
        -0.75
    ```
```