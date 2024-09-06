```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    for i in range(n):
        l[i] = l[i] + 1
    return l

# Test suite for incr_list function
def test_incr_list():
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert len(incr_list([10, 20, 30])) == 3
    assert incr_list([]) == []
```
The `incr_list` function increases the value of each element in the passed list by 1 and returns the updated list. The test suite ensures that the incr_list function works correctly for different inputs and produces the expected output.