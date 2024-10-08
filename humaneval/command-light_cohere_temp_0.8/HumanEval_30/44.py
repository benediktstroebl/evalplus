```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num > 0]

# Tests
def test_get_positive():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
    assert not get_positive([5, 0, -5])
    assert not get_positive([9, -9])
    assert not get_positive([10, -100])
``` 
The code defines a `get_positive` function that takes in a list and returns a new list containing only the positive numbers from the original list. It uses list comprehension and both iterating over each element and checking if the number is greater than zero, and returns the result as a new list.