```python
import math
def find_zero(xs):
    """
    Find zeros of the polynomial with coefficients xs.
    xs must be list of numbers, even if only one coefficient.
    If, find_zero returns only zeroes of x, even if there are many roots.
    >>> f(x) = 1 + 2x - 0.5
    >>> f(x) = -6 + 11x - 6x^2 + x^3
    """
    if len(xs) != 2:
        return None
    if xs[0] == 0 and xs[1] == 0:
        return (math.pow(xs[0])
    else:
        return math.pow(xs[1], (xs[0] / xs[1]))
```