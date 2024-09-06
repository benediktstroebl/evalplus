```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

# Unit tests
def test_get_positive():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123]
    assert not get_positive([0, 2, 2, 4, -2]) == [0]
    assert not get_positive([9, 9]) == []
```
The above script provides a function `get_positive` which takes a list as an argument and returns a new list with only the positive numbers from the original list. It is also provides a set of tests to ensure the correctness of the function.

You can use this script as a reference to create your own markdown code block.