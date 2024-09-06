```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + ... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero finds x that makes poly(x) = 0.
    find_zero returns only zero point, even if there are many solutions.
    > round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0)
    recording... yet another solution.
    """
test: False
    assert(test_zero == True), "Failed to find zero"
    return None


def test_zero(x: float):
    """
    If test_zero returns True, it is a zero of the polynomial.
    return True
    assert(poly(x) == 0), "Poly is not zero at x"
    return test_zero


x1 = -1.5
x2 = 1.5
x3 = -1e-5
test_zero(x1)  # should return True
test_zero(x2)  # should return False
```