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
    find_zero find x that makes poly(x) = 0, and returns only the zero point.
    find_zero returns only zero point, even if there are many roots.
    >round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    }
   
    assert find_zero([-6, 11, -6, 1]), -1
    assert find_zero([1, -1, 2, -3]), -1
    assert find_zero([1, -1, 2, -1, 2, 3]), 2
    assert find_zero([1, -2, 2, 3, -4]), 3
    """

poly([1, 2])  # returns 1 + 2x
```