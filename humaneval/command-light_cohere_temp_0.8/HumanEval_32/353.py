```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[-1] * x**(-1)

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0, returns only zero point, even if there are many.
    find_zero returns only zero point, however, it finds the zero point efficiently.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    """
   
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
   
   
   
    def test_find_zero(xs: list):
    return all([x >= 0 for x in find_zero(xs)])

# Example usage
xs = [1, 2]
test_xs = [1, -1]
test_ys = [1, 0]

if test_find_zero(xs):
    print("pass")
elif test_find_zero(test_xs):
    print("fail")
```
The function test_find_zero uses the find_zero function to check if it returns only zero points. It passes the and fails if it returns a non-zero point.