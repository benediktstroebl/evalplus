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
    find_zero find x such that polynomial(x) = 0, returns x.
    assert len(xs) % 2 == 0, "The list of coefficients must have even length, as the largest non-zero coefficient guarantees the existence of a solution."
    assert max(xs) != 0, "The list of coefficients must not have the same non-zero value, otherwise there is no solution."
    return x
```

The test cases use the `round` function to test the results of the `find_zero` function.  The test cases cover different combinations of coefficients and a point value.