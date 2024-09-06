```python
import math

def find_zero(xs):
    """
    Assume xs are coefficients of a polynomial
    f(x) = sum(xs * x**i for i, coeff in enumerate(xs))
    f(x) = 0
    """
    return math.floor(x / f(x))

xs = [1, 2]

# Test
assert find_zero(xs) == 0.0
assert round(find_zero(xs), 2) == 0
```