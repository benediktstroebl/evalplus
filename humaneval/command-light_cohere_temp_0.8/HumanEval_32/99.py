```python
import math
def find_zero(xs):
    assert len(xs) % 2 == 0, "List must have even number of coefficients."
    assert max(abs(xs[0])) <= 1, "First coefficient must be at most 1."
    assert max(abs(xs[i]) for i in range(1, len(xs))) <= 1 for i in xs[1:]
    return xs[0]
```