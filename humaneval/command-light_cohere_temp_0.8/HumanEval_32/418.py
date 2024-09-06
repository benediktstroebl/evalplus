```python
import math
def poly(xs: list, x: float) -> int:
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + .... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list) -> float:
    """
    xs are coefficients of a polynomial
    find_zero finds x that makes polynomial (xs)(x) = 0
    find_zero returns only x, even if there are many solutions.
    </p>.
    if len(xs) % 2 != 0:
        raise ValueError("The list must have even number of coefficients.")
    """
    x_val = -float('inf')
    while x_val**2 < xs[0]:
        x_val += 1
    return x_val
```