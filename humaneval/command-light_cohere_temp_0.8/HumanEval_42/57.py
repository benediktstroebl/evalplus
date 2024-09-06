```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test case 1
def test_incr_list():
    assert incr_list([1, 2, 3]) == [2, 3, 4]

# Test case 2
def test_incr_list2():
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
```
This script defines an `incr_list` function that adds 1 to each element in the passed list, and passes the test cases with various input lists. The test_incr_list2 function tests the `incr_list` function with different inputs and asserts the output is correct.