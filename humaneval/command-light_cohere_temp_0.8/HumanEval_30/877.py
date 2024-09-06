```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num > 0]

# Test the function
def test_get_positive():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
```
This code defines a `get_positive` function that takes a list of elements and returns a new list containing only the positive elements from the input. 

The function uses list comprehension to filter out the negative elements from the input list. 

Additionally, the code has a test function `test_get_positive` that uses the `get_positive` function to verify its correctness. 

This code is self-contained and effectively solves the problem of retrieving a list of only positive numbers from an input list of numbers, passing the test without errors.