```python
import math
def poly(xs):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])
def find_zero(xs):
    """
    xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0
    find_zero returns x
    """
    return math.floor(poly(xs)/xs[0]) if xs[0] != 0 else None
# Test the function
xs = [1, 2]
x = find_zero(xs)
if x is not None:
    print("Found zero:", x)
xs = [2,3,4,5]
x = find_zero(xs)
if x is not None:
    print("Found zero:", x)
```