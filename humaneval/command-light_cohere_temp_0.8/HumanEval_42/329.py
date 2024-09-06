```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test the function
test_incr_list = incr_list([1, 2, 3])
assert test_incr_list == [2, 3, 4]

test_incr_list_2 = incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
assert test_incr_list_2 == [6, 4, 6, 3, 4, 4, 10, 1, 124]
```
This script defines a function **incr_list** that takes a list as an argument and returns a new list with elements incremented by 1. The test cases demonstrate that the function is correct.