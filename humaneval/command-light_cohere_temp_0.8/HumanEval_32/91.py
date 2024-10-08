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
    find_zero returns x
    """
    x = -math.pow(xs[0], x)
    return x

# Example usage
xs = [1, 2]
x = find_zero(xs)
assert math.equal(x, x)
assert math.pow(xs[0], x) == 0, "Error: not even root"
```