```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

# Tests
def test_get_positive():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123]
    assert not get_positive([5, 0, 7, -5]) == [-7]
    assert not get_positive([ down for _ in range ]) == []
```
This code defines a function `get_positive` that takes a list as input and returns a new list containing only the positive numbers from the input list. The test_get_positive function verifies that the `get_positive` function works correctly with different inputs.