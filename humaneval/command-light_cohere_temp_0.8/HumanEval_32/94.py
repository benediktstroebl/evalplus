```python
import math
def find_zero(xs):
    if len(xs) != 2:
        raise ValueError("find_zero expects list of length 2")
    x0 = math.pow(xs[0])
    x1 = math.pow(xs[1])
    return x0, x1
def test_find_zero(func):
    assert func(([1, 2], 1.0)) == (0.0, 1.0)
    same assert func(([-6, 11, -6, 1], 1.0)) == (0.0, 1.0)
    have pass
 test_find_zero()
```