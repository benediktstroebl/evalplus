```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    l[:] = [x+1 for x in l]
    return l

# Test suite
def test_incr_list():
    assert incr_list([1, 2, 3]) == [2, 3, 4]

test_incr_list()
```
The function `incr_list` takes a list l as input and returns a new list with elements incremented by 1. The test suite ensures that the function works correctly by asserting that the output of the function is the expected result.