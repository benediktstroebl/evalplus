```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [i+1 for i in l]

# Test suite for function
def test_incr_list():
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert not incr_list([-1, 2, 3]) == [0]
    assert not incr_list([]) == []
```
The function incr_list takes a list l as input and returns a new list with elements incremented by 1. The test suite contains some tests that validate the correctness of the incr_list function.