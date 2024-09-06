```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

# Test suite
def test_get_positive():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
```
This code defines a function `get_positive` that takes a list as input and returns a new list containing only the positive numbers from the input list. The `test_get_positive` function contains unit tests that verify the correct behavior of the `get_positive` function. 
Please feel free to use and modify the script.