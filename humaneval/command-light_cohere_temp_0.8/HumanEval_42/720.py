```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    for i in range(n):
        l[i] = l[i] + 1
    return l

# Test function
def test_incr_list():
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert len(incr_list([99, 100, 101] )) == 3
    assert incr_list([]) == []
```
The provided Python script defines a function `incr_list` that returns a list with elements incremented by 1. The `test_incr_list` function is used to run tests on the `incr_list` function. The test function passes all test cases.