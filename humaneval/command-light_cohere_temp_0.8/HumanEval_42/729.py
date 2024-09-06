```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test function to check if the incr_list function works correctly
def test_incr_list():
    assert incr_list([1, 2, 3]) == [2, 3, 4]  # Should increment by 1 and get [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]  # Should increment by 1 and get the expected result

# Test case 1 passes
# Test case 2 passes

```
This Python script defines a function `incr_list` that takes a list `l` as an argument and returns a new list with elements incremented by 1. The test function `test_incr_list` is used to check if the `incr_list` function works correctly by passing in two lists and asserting that the result is as expected.