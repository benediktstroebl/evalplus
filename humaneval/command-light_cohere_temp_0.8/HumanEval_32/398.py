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
    find_zero finds x that makes polynomial(x) = 0.
    find_zero returns only zero point, even if there are many.
    Furthermore, find_zero only takes list xs having even number of coefficients and largest non zero coefficient as it guarantees a solution.
    # Test if the test of polynomial(x) = 0, by expanding and using polynomial long division.
    # Test if polynomial is x^n = 1, by evaluating polynomial at x = 0
    # Test for correct result of polynomial division
    xs = [1, 2, -6, 11, -6, 1]
    x = 0.5
    y = poly(xs, x)
    assert y == 0
    # Test for correct result of polynomial long division
    xs = [1, 2, -6, 11, -6, 1]
    x = 0.1
    y = poly(xs, x)
    assert y == 0
    # Test if polynomial has solution
    xs = [2, -2, 3, -5, 0, 1]
    x = 4
    y = poly(xs, x)
    assert y != 0
```