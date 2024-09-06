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
    find_zero find x such that the polynomial is equal to zero
    find_zero returns the value of the variable x
    """
    return round(poly(xs, 0), 2)

# Test the function with an example input
xs = [1, 2]
x = 3.6
print(find_zero(xs))  # Output: 1.0
```

The test code has a list of coefficients xs and a test value x. The function `find_zero` returns the zero value of the polynomial with those coefficients evaluated at x.