```python
import math
def find_zero(xs):
    assert len(xs) % 2 == 0
    assert all(xs) >= 0
    assert math.pow(xs[-1], -1) == 0, "Last coefficient should be -1"
    assert math.pow(xs[0], -1) == 0, "First coefficient should be 1"
    return xs[0]
```