```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + .... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x that makes polynomial equal to 0, and return only the root, even if there are many roots.
    >.1
        return only zero polynomial in xs if it has even number of coefficients and the largest non zero coefficient, because this is what guarantees a solution.
    }.
    # > rounding the br Tags to 2 to match the way the code works
    > return round(find_zero([1, 2]), 2)
    > return find_zero([-6, 11, -6, 1]), 2) # (-6 + 11x - 6x^2 + x^3)
    > return find_zero([6, 11, -6, 1]), 2) # (6 + 11x - 6x^2 + x^3)
    > return find_zero([1, -3, 1, -1]), 2) # (x + 3) * (x - 1)
    -1.0
    """
 > return find_zero([1, -3, 1, -1], 1.0) # (x - 1 + 3) * (x - 1)
-1.0)
```