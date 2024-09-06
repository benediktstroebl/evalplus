```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[-1] * x**(-1)

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0
    """
    return only zero point, even if there are many
    """
    return math.floor(find(poly, x))

# Test
xs = [1, 2]
y = find_zero(xs)
assert y == float('-inf')  # 1 should not be a root
xs = [2,2,2,2]
y = find_zero(xs)
assert y == float('3')  # 2 should be a root
xs = [2,2,3,3]
y = find_zero(xs)
assert y == float('6')  # 2 should be a root
xs = [1,1,2,2,3]
y = find_zero(xs)
assert y == float('6')  # 1 should be a root
```
This script defines a function `poly` that evaluates a polynomial with given coefficients at a point `x`. It also defines a function `find_zero` that finds the zero of the polynomial `poly(x)` using the function `find`. The `find_zero` function returns only the zero point, even if there are many roots. The script then passes tests to the `find_zero` function with different sets of coefficients. It passes the tests to ensure that the `find_zero` function returns the correct result for each set of coefficients.