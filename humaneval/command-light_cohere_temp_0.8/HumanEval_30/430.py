```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test suite
def test_get_positive():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
    assert not get_positive([-100, 2])
    assert not get_positive([1, 2, 3, -100])
```
The code defines a function, `get_positive`, that takes an input list and returns a new list containing only the positive numbers from the input. It uses list comprehension with the  a list comprehension condition `num >= 0` to filter out negative numbers.  The run-time tests to ensure that the function works correctly.