```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

# Unit tests
def test_get_positive():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123]
    assert not get_positive([5, 0, -5])
    assert not get_positive([9, -9])
```
The code defines a function get_positive that takes a list lst as input and returns a new list containing only the positive numbers from the original list. It uses list comprehension with the specific conditions to achieve this. The function is then tested using unittesting with the help of the test_get_positive function.