```python
import math
def find_zero(xs):
    assert len(xs) % 2 == 0
    assert all(abs(x) <= 1 for x in xs), "All coefficients must be less than 1"
    assert math.isumpow(xs),
    return xs[0]

xs = [1, 2]
assert find_zero(xs) == 0
assert all(xs[0] > 0)
assert all(xs[0] <= 1)
xs = [-6, 11, -6, 1]
assert find_zero(xs) == -6
```