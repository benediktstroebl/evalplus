```python
import math
def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])
def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero finds x that makes poly(x) = 0
    find_zero returns only zero point, even if there are many.
    return the maximum non zero coefficient and x
    """
    if len(xs) % 2 != 0:
        raise ValueError("find_zero requires list xs having even number of coefficients")
    if len(xs) == 2:
        return float(xs[0]) * x + xs[1]
    elif len(xs) > 2:
        return xs[0] * x + xs[1] + xs[2] * x**2
    else:
        return 0
```