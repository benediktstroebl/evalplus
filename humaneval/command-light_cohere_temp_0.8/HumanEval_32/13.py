```python
import math
def find_zero(xs):
    assert len(xs) % 2 == 0
    assert all(xs[i] != 0 for i, x in enumerate(xs) if x != 0)
    assert xs[-1] >= 0
    return xs[-1]
def poly(xs, x):
    assert len(xs) > 1
    return sum([xs[i] * math.pow(x, i) for i, coeff in enumerate(xs)])
if __name__ == "__main__":
    assert find_zero([1, 2]) == 2
    assert find_zero([1, 2, -3]) == -3
    assert find_zero([-6, 11, -6, 1]) == 1
    assert poly(xs=[1, 2, -3], x=4) == -6
    assert poly(xs=[-6, 11, -6, 1], x=2) == 11
```