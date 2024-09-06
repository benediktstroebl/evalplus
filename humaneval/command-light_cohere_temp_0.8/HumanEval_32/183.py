```python
import math
def find_zero(xs):
    """
    >>> round(find_zero([1, 2])) # f(x) = 1 + 2x -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
   
   
    >>> round(find_zero([1, 2, 3]), 2) # f(x) = 1 + 2x -3
    -0.5
    >>> round(find_zero([1, 2, 4, 5]), 2) # f(x) = 1 + 2x + 4x^2 - 5x^3
    1.0)
   
   
    """
    return sum([i*math.pow(x, i) for i, coeff in enumerate(xs)]) == 0
```