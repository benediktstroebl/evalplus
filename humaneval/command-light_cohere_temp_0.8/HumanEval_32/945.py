```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero finds x such that polynomial(x) = 0.
    find_zero returns only zero point, even if there are many solutions.
    return the x if xs[0] != 0 and the list has even number of coefficients
    and the largest non zero coefficient is greater than 0
    """
    if xs[0] != 0 and len(xs) % 2 != 0:
        return xs[0]
    elif len(xs) % 2 == 0:
        return -xs[0]
    else:
        return None
```