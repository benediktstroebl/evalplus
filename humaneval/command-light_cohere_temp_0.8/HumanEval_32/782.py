```python
import math
def find_zero(xs):
    """
    Find zeroes of the polynomial
    >>> find_zero([1,2])  # returns (1,1)
    >>> find_zero([6,11,-6,1])  # returns (1,-1)
    """
    if len(xs) % 2 != 0:
        raise ValueError("The list must have an even number of coefficients")
    return list(map(lambda x: x if x != 0 else 0, xs))
```
The function returns the zeroes of the polynomial passed as an argument.