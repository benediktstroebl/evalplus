```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num > 0]

#Test the function
def test_get_positive():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123]
```
The `get_positive` function filters out the negative numbers and returns a new list containing only the positive numbers from the input list. 
The test_get_positive function uses the `assert` statement to check if the `get_positive` function is correctly calling and returning the expected results.