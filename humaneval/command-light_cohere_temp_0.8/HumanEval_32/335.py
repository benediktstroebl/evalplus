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

    If xs has an odd number of coefficients, return None.
    if len(xs) == 0:
        return None
    elif len(xs) == 1:
        return float(xs[0])
    elif len(xs) % 2 == 0:
        # largest non zero coefficient guarantees a solution
        return max(xs)
    else:
        # need to determine the leading coefficient
        # determine the leading coefficient and subtract from all xs
        x0 = 0
        for i, coeff in enumerate(xs):
            x0 += coeff * math.pow(i, x)
        return x0
```