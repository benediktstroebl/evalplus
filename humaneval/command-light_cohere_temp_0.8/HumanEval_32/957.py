```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + .... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x that makes poly(x) = 0.
    find_zero returns only zero point, even if there are many roots.
    assert all(x != 0 for x in xs), "Coefficients have no roots"
    assert len(xs) == len(xs[0]) // 2, "Length of xs does not divide evenly by 2"
    find_zero_double = lambda x: xs[0] * x + xs[1] * (x**2 - 4 * x * x - 3)
    find_zero_half = lambda x: xs[0] * x + xs[1] * x**2
    return find_zero_half(max(x for x in find_zero_double()))
```