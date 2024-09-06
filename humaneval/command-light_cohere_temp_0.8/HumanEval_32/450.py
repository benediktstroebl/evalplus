```python
import math
def find_zero(xs):
    """
    Find the x value at which polynomial is zero
    >>> find_zero([1, 2])  # returns 1.0
    >>> find_zero([-6, 11, -6, 1])  # returns 1.0
    """
    pattern: List must have even number of coefficients
    """
    assert len(xs) % 2 == 0
    assert max(abs(xs[i]) for i in range(len(xs))) == 0
    assert xs[-1] != 0
    return xs[-1]
```