```python
import math
def find_zero(xs):
    """
    Find polynomial zero using the rational root test.
    xs = [list(xs)
    r = 2  # Test number
    for i, x in enumerate(xs):
        if x == r:
            return i
    return None  # No solution found
def test_find_zero(test_xs):
    """
    Test list of coefficients xs
    and expected result for find_zero
    Test list: [1, 2]
    Result: 0
    """
    test_xs = [1, 2]
    test_result = find_zero(test_xs)
    assert test_result == 0, "Expected 0, found " + str(test_result) + " instead."
```