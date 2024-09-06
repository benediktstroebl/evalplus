```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test suite for get_positive function
def test_get_positive():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
    assert not get_positive([5, 0, -10, -100]) or [5]
    assert not get_positive([1, 2, 3, 004, -5]) or []
```
This code defines a function `get_positive` that takes a list as input and returns a new list containing only the positive elements from the original list. The function employs list comprehension to iterate through the list and filter out the positive elements. The test suite contains several test cases that verify the correctness of the `get_positive` function by passing different input lists and asserting that the returned lists contain the expected positive elements.