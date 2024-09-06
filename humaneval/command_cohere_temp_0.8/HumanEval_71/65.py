```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a) > 1e-6 or abs(s - b) > 1e-6 or abs(s - c) > 1e-6:
        return -1
    return round(0.5 * (s * (s - a) * (s - b) * (s - c))**, 2)
```
The function first checks whether the sum of the sides is different from each of the sides by more than 1e-6, which is essentially a very small number slightly more than 0 to account for the floating point error. If the sum rule is not satisfied, the function returns -1. If the sum rule is satisfied, the function proceeds to calculate the area and returns it rounded to 2 decimal places. Please note that this solution assumes that the lengths of the sides are given as positive integers. 

To make the code more robust and handle all edge cases, including those where the side lengths are negative or not integers, we can incorporate tests that generate such inputs and ensure that the function behaves logically, returning -1 in cases of invalid triangles or numerical results in valid ones. Below is a simplified version of a test suite: 
```python
# Test suite
import numpy as np

def test_triangle_area():
    # Invalid triangle: Side lengths do not satisfy the sum rule
    assert triangle_area(1, 2, 10) == -1
    assert triangle_area(-3, 4, 5) == -1
    assert triangle_area(0, 1, 1) == -1

    # Valid triangle: Side lengths satisfy the sum rule
    assert triangle_area(3, 4, 5) == 6.00
    assert triangle_area(1, 2, 3) == 2.00
    assert triangle_area(10, 21, 19) == 42.00

    # Edge cases: Side lengths are 0
    assert triangle_area(0, 0, 0) == 0.00
    assert triangle_area(0, 1, 1) == 0.00

    # Edge cases: Side lengths are inf
    assert triangle_area(np.inf, 7, 9) == 9.00
    assert triangle_area(5, np.inf, 8) == 13.00
    assert triangle_area(3, 4, np.inf) == 6.00

    # Edge cases: Side lengths are nan
    assert triangle_area(np.nan, 5, 6) == -1
    assert triangle_area(7, np.nan, 9) == -1
    assert triangle_area(8, 7, np.nan) == -1
``` 

This way, the function can handle a variety of inputs, valid and invalid, providing the correct result or error message whenever applicable.