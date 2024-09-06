```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test the function
def test_get_positive():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123]
```
The `get_positive` function takes a list as an argument and returns a new list containing only the positive numbers from the input list. The test_get_positive function is used to test the correctness of the `get_positive` function by passing various input lists and asserting that the function returns the expected output.