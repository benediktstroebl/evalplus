```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    new_list = [x + 1 for x in l]
    return new_list

# Test function for incr_list
def test_incr_list():
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert not incr_list([]) == []
    assert not incr_list([5, 9, 0]) == [5, 9, 0]
```
The provided Python script defines a function `incr_list` that takes a list as input and returns a new list with elements incremented by 1. The `test_incr_list` function contains a series of assertions that validate the correctness of the `incr_list` function.