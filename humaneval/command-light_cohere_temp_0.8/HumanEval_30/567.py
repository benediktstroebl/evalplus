```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Unit tests
def test_get_positive():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
    assert not get_positive([10, 2, 3, -20]) or [10, 2, 3, -20] is None
    assert not get_positive([]) or [()] is None
```
The code defines a function **get_positive** that takes a list as an argument and returns a new list with only the positive elements from the original list. The unit tests section verifies the