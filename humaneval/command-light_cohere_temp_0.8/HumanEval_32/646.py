```python
import math
def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero find x such that the polynomial is equal to zero.
    find_zero returns only zero point, even if there are many solutions
    and ensures that the coefficients list has an even number of elements, and the largest non-zero coefficient is used to find the solution.
    return round(x, 2)
    """
    return round(find_zero([1, 2]), 2)
    assert round(find_zero([-6, 11, -6, 1]), 2) == (x - 1) * (x - 2) * (x - 3)
    assert round(find_zero([1, -3, 2, -4]), 2) == (x + 1) * (x - 2)
    assert round(find_zero([1, -4, 2, -6, -5]), 2) == (x + 2) * (x - 6)
    assert round(find_zero([1, -6, -8, 2, -4, -3]), 2) == (x + 3) * (x - 4)
    assert round(find_zero([-1, -6, -8, 2, -4, -3]), 2) == x
    assert round(find_zero([-1, -8, -6, 2, -4, -3]), 2) != x
    assert round(find_zero([-1, -8, -6, -2, -4, -3]), 2) != x
    assert round(find_zero([-1, -8, -6, -8, -4, -3]), 2) == x
    assert round(find_zero([-1, -8, -6, -8, -4, -3, -2]), 2) == x
    return x
```