```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [i+1 for i in l]

def test_incr_list():
    """docstring for test function"""
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert incr_list([]) == []
    assert incr_list([5, 6, 7]) == [6, 7, 8]
```
The provided code defines a function `incr_list` that increments elements of a given list by 1 and returns the modified list. It also contains a specific test function that passes all the test cases.