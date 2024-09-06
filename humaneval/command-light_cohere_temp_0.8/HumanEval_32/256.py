```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[-1] * x**(-1)

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero finds x that makes poly(x) = 0.
    find_zero returns only zero point, even if there are many solutions.
    and finds_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees a solution.

    Test cases:
    >>> poly(x, 0)  # returns x**0
    >>> poly([1, 0])(1)  # returns 1
    >>> poly(x) = 0  # raises error
    """
    return math.pow(x, 0.0)
```