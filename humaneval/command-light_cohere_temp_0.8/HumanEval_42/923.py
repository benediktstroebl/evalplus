```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [x + 1 for x in l]
    return result

# Test function to check if incr_list works correctly
def test_incr_list():
    l = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    expected = [6, 4, 6, 3, 4, 4, 10, 1, 124]
    got = incr_list(l)
    assert got == expected, "Incorrect result"
```
This script defines a function `incr_list` that takes a list `l` as an argument and returns a new list with elements from `l` incremented by 1. The `test_incr_list` function is used to check if the `incr_list` function works correctly by passing the list `[5, 3, 5, 2, 3, 3, 3, 9, 0, 123]` as an argument and comparing the `result` with the `expected` list. 
script also passes all the test cases and checks if the `assert` statement is True, which indicates that the `incr_list` function is working correctly.