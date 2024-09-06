```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero finds x that makes poly(x) = 0.
    find_zero returns only zero point, even if there are many solutions.
    # test if it passes 2 tests:
    assert all(abs(poly(x)) < 1e-12)
    assert math.isinrange(-1, 1) (poly(x))
    return x[0]
    """
    # check 2 tests
    assert all(abs(poly(x)) < 1e-12)
    assert math.isinrange(-1, 1) (poly(x))
    return x[0]


# test the function
x = find_zero([1, 2])
print(x)
```