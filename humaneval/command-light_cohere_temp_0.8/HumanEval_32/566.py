```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[-1] * x**(-1)

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero finds x such that poly(x) = 0
    find_zero returns only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients and largest non-zero coefficient as it guarantees a solution.

    Test cases:
    - test find_zero([1, 2])
        - test find_zero([-6, 11, -6, 1])
    """
    return math.floor(find_zero(xs, x=0.0))
```