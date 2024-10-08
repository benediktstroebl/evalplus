```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[-1] * x**(-n)
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0.
    find_zero returns only zero point, even if there are many solutions.
    and find_zero only takes list xs having even number of coefficients and largest non zero coefficient as it guarantees a solution.
    assert all(abs(x) > 0 for x in find_zero), "Zeroes cannot be negative."
    return [x[0]]

xs = [1, 2]
poly(xs, 3) # Output: 4
assert len(find_zero(xs)) == 1, "Length should be even"
assert x[0] == 2, "First zero is incorrect"
```