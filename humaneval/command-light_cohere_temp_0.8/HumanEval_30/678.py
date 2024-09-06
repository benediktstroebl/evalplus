```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test suite
def test_get_positive():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
```
The function `get_positive` takes a list as input and returns a new list with only the positive elements from the original input list. 
The `test_get_positive` function contains tests that validate the correctness of the `get_positive` function with various input lists.