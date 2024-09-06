```python
import math
def find_zero(xs):
    assert len(xs) % 2 == 0, "Coefficients list must have an even number of elements."
    assert max(abs(x) for x in xs) <= 1, "Largest coefficient must be less than or equal to 1."

    x = xs[0] / max(abs(x) for x in xs)
    return x
```