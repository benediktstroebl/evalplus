```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x that makes polynomial equal to 0.
    find_zero returns only zero point, even if there are many.
    """
   , find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    return (x, coeff[0])  # return first element of tuple x, coeff[0] = root

# Test cases
xs = [1, 2]
xs_even = [2, 2]
xs_odd = [-6, 11, -6, 1]

assert poly(xs, 2) == 3
assert poly(xs_even, 2) == 2
assert poly(xs_odd, 2) == -1

assert find_zero(xs) == (2, 1)

assert find_zero(xs_even) == (2, 2)

assert find_zero(xs_odd) == (-1, 1)
```