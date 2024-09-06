```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + .... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero find x that makes poly(x) = 0, where poly(x) is evaluated at x
    using the above poly() function.
    find_zero returns only zero point, even if there are many solutions.
    # Test if all coefficients are non-zero
    assert all(c != 0 for c in xs), fail otherwise
    assert math.isclose(), fail otherwise
    thin(xs)  # assert each coefficient less than one
    for c in xs:
        assert c < 1.0, fail
    assert math.is(-c) <= 0.0 <= 1.0, fail otherwise
    thin(xs)
    # Test if function returns correct result for given input
    assert poly(xs, x) == 0, fail otherwise
    return x

xs = [1, 2]
x = find_zero(xs)
print(x)
```