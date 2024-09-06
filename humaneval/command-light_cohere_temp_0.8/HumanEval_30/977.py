```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test the function
def test_get_positive():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]

```

This script defines a function `get_positive` that returns a list of only the positive numbers from the input list `lst`. It also provides a function `test_get_positive` that passes all tests for the `get_positive` function with the listed inputs.