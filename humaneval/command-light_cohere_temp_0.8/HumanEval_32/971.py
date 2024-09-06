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
    find_zero returns only zero point, even if there are many roots.
    """
    note that find_zero only takes lists xs having even number of coefficients
    and largest non zero coefficient as it guarantees a solution.
    """
    int len(xs)
    assert len(xs) % 2 == 0, "Inconsistent input: coefficients list must have even length."
    if xs[0] != 0:
        return float('inf')
    return math.floor(math.poly(xs[0])
```

This script defines two functions: `poly` evaluates the polynomial at a given point `x`, and `find_zero` finds the zero of a polynomial `poly(x)`. The `find_zero` function returns the x-coordinate of the root, or `float('inf')` if the polynomial has no root.  The root is the largest coefficient in the list.