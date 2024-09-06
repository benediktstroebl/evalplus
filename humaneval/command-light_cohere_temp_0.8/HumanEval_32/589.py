```python
import math
def find_zero(xs):
    if len(xs) != 2:
        raise ValueError("Input must be a list of size 2")
    coef1, coef2 = xs
    root1 = math.sqrt(max(coef1, coef2))
    x0 = (coef1 + coef2) / (root1**2)
    return x0
def test_find_zero():
    x = find_zero([1, 2])
    assert x == 0.0
    print("Test passed")
```