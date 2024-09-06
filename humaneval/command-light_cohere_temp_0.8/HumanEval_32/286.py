```python
import math
def find_zero(xs):
    assert len(xs) % 2 == 0
    assert max(abs(xs[i]) for i in range(len(xs))) <= 1
    assert all(xs[i] == 0 for i in range(len(xs)) - 1))
    return xs[0]
def poly(xs: list, x: float):
    return sum([xs[i] * math.pow(x, i) for i in range(len(xs))])
def test_find_zero():
    assert find_zero([1, 2]) == 0.0
    assert find_zero([-6, 11, -6, 1]) == 1.0
    ```