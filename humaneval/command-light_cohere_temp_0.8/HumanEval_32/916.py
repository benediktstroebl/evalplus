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
    find_zero find x that makes the polynomial equal to 0
    find_zero returns only zero point, even if there are many.
    ensure that xs have even number of coefficients and the largest non zero coefficient as it guarantees
    a solution.
```
xs = [1, 2]
poly(xs, 3)
print(find_zero(xs))

xs = [1, -6, 11, -6, 1]
poly(xs, 3)
print(find_zero(xs))

xs = [1, 2, 3, 0, -1]
poly(xs, 2)
print(find_zero(xs))

```
We evaluate the polynomial function and test the function with different coefficients and degrees. The find_zero function returns the minimum of two possible solutions.