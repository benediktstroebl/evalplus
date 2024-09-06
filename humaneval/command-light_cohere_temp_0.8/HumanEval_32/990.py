```python
import math

def find_zero(xs):
    """
    xs are coefficients of a polynomial
    find_zero returns only zero point, even if there are many.
    However, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """ test a test and returns a list of all zeroes
    """
    coefficients = [x**i // i**2 for i, x in enumerate(xs)]
    return coefficients
if not coefficients:
    return None
    else:
        return [x for x in coefficients if x == 0]
```