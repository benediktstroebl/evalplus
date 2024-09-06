```python
import math
def find_zero(xs):
    if len(xs) != 2:
        raise ValueError("find_zero takes list of length 2.")
    if xs[0] == 0 and xs[1] == 0:
        return (0, 0)
    elif xs[0] > 0 and xs[1] == 0:
        return (xs[0], 0)
    elif xs[0] == 0 and xs[1] > 0:
        return (0, xs[1])
    elif xs[1] == 0 and xs[0] > 0:
        return (xs[0], 0)
    else:
        return (-xs[0], -xs[1])
def test_find_zero():
    x1 = [1, 2]
    x2 = [-6, 11, -6, 1]
    result = find_zero(x1)
    assert result == (0, 0)
    result = find_zero(x2)
    assert result == (-6, 11)
```