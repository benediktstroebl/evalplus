```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [i+1 for i in l]

# Test suite
def test_incr_list():
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert len(incr_list([99, 45, 20])) == 3
    assert len(incr_list([99, 45, 4]))) == 0
    assert incr_list([]) == []
```
The code defines an incr_list function that adds 1 to each element in the input list and a test suite with several assertions that validate the correctness of the incr_list function. The test_incr_list function verifies that the incr_list function produces the expected output for various input lists and satisfies the length condition for empty lists.