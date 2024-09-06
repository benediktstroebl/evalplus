```python
import math
def poly(xs: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])
def find_zero(xs: list) -> float:
    """ xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0
    """
    return math.floor(poly(x, xs) == 0)
# Test suite
    assert find_zero([1, 2]) == 0
    assert find_zero([-6, 11, -6, 1]) == 0
```
The test suite checks that the `find_zero` function returns the correct results when given test cases.