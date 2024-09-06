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
    find_zero find x such that poly(x) = 0
    find_zero returns x, but it's recommended to return only zero if there are many roots
    and non-zero coefficients.

test_poly = [1, 2]
test_find_zero = find_zero(test_poly)
assert test_find_zero == 0.5, "Failed to find any roots"

test_poly = [1, -6, 11, -6]
test_find_zero = find_zero(test_poly)
assert test_find_zero == -6.5, "Failed to find any roots"

test_poly = [2, -1, -3]
test_find_zero = find_zero(test_poly)
assert test_find_zero == -1.25, "Failed to find any roots"
```
The code defines a function `poly` that computes the polynomial result for a given list of coefficients and a point `x`. The `find_zero` function searches for the zero point of the polynomial. Finally, it tests the script provides two examples to test the `poly` and `find_zero` functions, and verifies the functions using the `assert` assertion.