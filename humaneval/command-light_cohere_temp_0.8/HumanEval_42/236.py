```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    res = [0] * (n+1)
    for i in range(n): res[i+1] = l[i] + 1
    return res

def test_incr_list():
    """Test incr_list function."""
    lst = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    expected = [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert list(incr_list(lst)) == expected
```
The provided function `incr_list` takes a list as an argument and returns a new list with elements incremented by 1. The test function `test_incr_list` tests the `incr_list` function with a sample list and checks if the result is correct.

The `incr_list` function can be used to increment the elements of any list, and the test function can be used to verify that the function is working correctly with a list of any elements.