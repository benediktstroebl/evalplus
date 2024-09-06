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
    find_zero find x such that polynomial(x) = 0, returns only zero point, even if there are many roots. The function, takes list xs having even number of coefficients, and largest non zero coefficient as a starting point
    """
    assert len(xs) % 2 != 0, "Error: number of coefficients must be even."
    assert len(xs) >= 2, "Error: number of coefficients must be at least two"
    assert xs[0] != 0, "Error: must have a non-zero coefficient"
    assert xs[0] != 1, "Error: must not have a multiplicative constant"
    x1 = xs[0] / math.factmax(abs(xs[1:]))
    x = x1 + xs[1] / math.pow(x1)
    assert x < 1.0 and x >= 0.0, "Error: x must be in the interval [0, 1]"
    break;
```