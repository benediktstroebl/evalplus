```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[-1] * x**(-n)
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero find x such that polynomial(x) = 0.
    find_zero returns only zero point, even if there are many.
    >! existence of a polynomial is a sequence of numbers, so there is exactly one zero.
    # In order using a code, we can simply return the first element in xs.
    "
    return 0"
```