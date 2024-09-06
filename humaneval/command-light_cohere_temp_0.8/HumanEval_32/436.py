```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[-1] * x**(-1)

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0
    find_zero returns x even if there are many solutions, but only returns the first solution encountered.

    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    # True
    >>
    """

```