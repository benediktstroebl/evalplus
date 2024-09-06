```python
import math
def find_zero(xs):
    """
    xs are coefficients of a polynomial
    find_zero find x such that polynomial xs(x) = 0
    find_zero returns x or x = inf if there is no root
    """
    if len(xs) % 2 == 0:
        return min(xs[i] for i in range(len(xs)//2))
    else:
        return float('inf')
```