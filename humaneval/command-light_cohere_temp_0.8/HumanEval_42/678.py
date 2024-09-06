```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    l.append(1)
    return l

def test_incr_list():
    """Test the incr_list function."""
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
```
The provided Python code defines a function `incr_list` that appends a value of 1 to each element in a given list and then returns the updated list. The `test_incr_list` function contains a test suite for the `incr_list` function, ensuring that it correctly operates on various input lists.