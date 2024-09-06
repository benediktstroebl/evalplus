```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test the function
def test_get_positive():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123]
    assert len(get_positive([9, 7, 4, 1])) == 3
    assert len(get_positive([-9, -7, -4]))) == 3
    assert get_positive([1, 2, 3, 4, -3]) == [1, 2, 3]
```
This code defines a function `get_positive` that returns a list containing only the positive numbers from the input list. It also provides a specific test cases to ensure the function works as expected.