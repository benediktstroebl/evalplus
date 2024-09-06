```python
import math

def find_zero(xs):
    """
    Assume input is a list of coefficients of a polynomial
    Find and return the zero of a polynomial f(x) using the method in poly(). Somewhat faster.
    Assume that largest coefficient is non-zero and the corresponding x value.
    return only the value: x
    """
    return x  # x = xs[0]

def poly(xs, x):
    """
    # evaluate polynomial f(x) with coefficients xs at point x
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[-1] * x**n
    """
    return sum([xs[i] * math.pow(x, i) for i, coeff in enumerate(xs)])

# test
xs = [1, 2,3]
x = 0.5
ans = poly(xs,x)
assert_equal(ans,0.0, "find_zero failed")
```