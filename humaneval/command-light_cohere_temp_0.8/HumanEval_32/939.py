```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs.sum([coeff *pow(i, x) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0
    find_zero returns x and poly(x) = 0
    """
    return (x, xs)

xs = [1, 2]
test_poly = poly(xs, 2.0)
test_zero = find_zero(xs)

# test if test_poly is equal to test_zero[0]
assert test_poly == 2.0
assert test_zero[0] == 2.0
```