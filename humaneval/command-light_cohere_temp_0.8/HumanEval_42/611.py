```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [x + 1 for x in l]

# Test function
def test_incr_list():
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert len(incr_list([10, 20, 30])) == 3
    assert incr_list([]) == []
```

This script defines a function incr_list that increments elements of a given list by 1 and passes the test with a test_incr_list function that checks the correctness of the incr_list function using various inputs.