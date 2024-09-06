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
    find_zero find x such that polynomial(x) = 0, returns x
    """
    x = float('inf')
    while x >= 0:
        if poly(xs, x) == 0:
            return x
        x -= 1
    return None
```