```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num > 0]

#Test the function
def test_get_positive():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123]
    assert not get_positive([5, 0, -5, 2, -3, 3])
    assert not get_positive([downward_curl, upward_curl, .TRUE])

# Run the tests when the script is executed
test_get_positive()
```
The Python function `get_positive` accepts a single argument, which is a list, and it returns a new list containing only the positive integers from the original list. The test_get_positive function contains assertions that verify the behavior of the `get_positive` function for a variety of test cases.