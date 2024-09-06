```python
import math
def find_zero(xs):
    if len(xs) != len(xs[0]):
        raise ValueError("Input list must have even number of coefficients")
    return math.pow(xs[0])
```
The function 'find_zero' finds the zeroth element of the polynomial p(x) by passing the coefficients of the polynomial as input. It works by using the largest nonzero coefficient as a starting point, which guarantees that the polynomial has a root.