```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    l.extend(1)
    l.append(1)
    return l

def test_incr_list():
    """Test function."""
    lst = [1, 2, 3]
    assert incr_list(lst) == [2, 3, 4]
    lst = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    assert incr_list(lst) == [6, 4, 6, 3, 4, 4, 10, 1, 124]

# Test with input argument
test_incr_list()
```

This code defines the `incr_list` function, which simply returns a new list with elements incremented by 1. The `test_incr_list` function tests the `incr_list` function by creating two lists with different values and then asserting that the result of the `incr_list` function is correct.