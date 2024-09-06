```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[-1] * x**(-1)
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero finds x that makes polynomial(x) = 0
    find_zero returns only zero point, even if there are many.
    assert len(xs) == even, "Error: Input must have an even number of coefficients"
    assert xs[-1] != 0, "Error: Input must not have a zero coefficient"
    return math.floor(math.pow(xs[-1], x) / math.pow(xs[-1]))
```

This script defines two functions: 
- `poly()` evaluates the given polynomial at a given point.
- `find_zero()` finds the root of the polynomial by calculating the zero of the denominator by the last coefficient of the polynomial.