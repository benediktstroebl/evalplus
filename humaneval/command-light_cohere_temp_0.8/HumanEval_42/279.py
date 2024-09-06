```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    n = len(l)
    result = [x + 1 for x in l]
    assert len(result) == n
    assert all(result[i] == i + 1 for i in range(n))
    return result

# Test suite
def test_incr_list():
    import_list(range(10))
    result = incr_list(l)
    assert result == [i + 1 for i in range(10)]
    assert incr_list([0, 1, 2]) == [1, 2, 3]
    assert incr_list([3, 3, 4, 3]) == [4, 5, 6]
    assert incr_list([100, 101, 102]) == [101, 103, 104]
```
The `incr_list` function accepts a list `l` and returns a new list with elements incremented by 1. The test suite verifies that `incr_list` function by creating a list of numbers, passing it to `incr_list` and checking the resulting list against the expected output.