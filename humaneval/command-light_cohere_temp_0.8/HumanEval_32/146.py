```python
import math
def find_zero(xs):
    assert len(xs) % 2 == 0, "Coefficients list must have an even number of elements."
    assert max(abs(xs[i])) <= 1, "Largest non-zero coefficient must be exactly 1."
    return xs[0]
```