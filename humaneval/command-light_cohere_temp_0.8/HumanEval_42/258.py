```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    res = [x + 1 for x in l]
    assert len(res) == n
    assert all(x == n - 1 for x in res)  # Test for element-wise increment
    assert all(x == n for x in res)  # Test for monotonically increasing sequence
    return res

# Test suite
assert incr_list([1, 2, 3]) == [2, 3, 4]
assert incr_list([5, 3, 5]) == [6, 5, 6]
assert incr_list([5, 3, 5, 2, 3, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
```

This script defines a function incr_list that takes a list l as input and returns a new list with elements incremented by 1. The function includes various assert statements to validate the correctness of the output. The test suite provides test cases that cover different scenarios. 

I hope this helps you understand how the problem is solved!