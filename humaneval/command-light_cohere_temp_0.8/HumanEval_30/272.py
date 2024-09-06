```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test suite
def test_get_positive():
    assert get_positive([1, 2, -3, -4, 5, 6]) == [1, 2, 4, 5, 6]
    assert get_positive([-1, 2, -4, 5, 6]) == [1, 2, 4, 5]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123]
    assert get_positive([]) == []
    assert get_positive([20, 33, -55]) == []
```
This script defines a function `get_positive` that takes a list as input and returns a new list containing only the positive elements from the original list. It also contains a use a `test_get_positive` function to test the `get_positive` function with various input lists.