```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero finds x that makes the polynomial equal to zero, returns only zero point, and always returns a list.
    return [list(xs) having even number of coefficients and the largest non-zero coefficient as it guarantees a solution.
    """
    return [list([x for x in xs if math.iscloseequal(poly(xs, x), 0)])
```