```python
import math
def find_zero(xs):
    if len(xs) != len(set(xs)):
        raise ValueError("Input list must be unordered and have the same number of elements")
    if len(xs) < 2:
        raise ValueError("At least two elements required for polynomial interpolation.")
    # sort the list and find the largest non-zero coefficient
    largest = max(xs)
    xs.sort(key=lambda x: x/largest)
    zero_coeff = float(xs[0])
    xs.remove(xs[0])
    # use polynomial interpolation to find zero
    ys = [x*xs[i] for i, x in enumerate(xs)]
    y = [0]
    for i, x in enumerate(xs):
        y.append(ys[i] * (x-zero_coeff) + ys[i]
    return y
# pass tests
try:
    assert find_zero([1,2]) == [-0.5, 1.2]
    assert find_zero([-6,11,-6,1]) == [-6, 11, -6,1]
    assert find_zero([-5, -4, -5, -5, -5, -5, -5, -5, -5, -5]) == [-0, -0, -0, -0, -0, -0, -0, -0]
except AssertionError as e:
        print("Errors:", e)
```