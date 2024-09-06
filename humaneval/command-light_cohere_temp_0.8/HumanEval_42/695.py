```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test case 1
assert incr_list([1, 2, 3]) == [2, 3, 4]

# Test case 2
assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
```
This script defines a function `incr_list` that takes a list l as input and returns a new list with elements incremented by 1. The function works by using a list comprehension with the `+ 1` expression, which adds 1 to each element of the input list. The test cases demonstrate that this function is correct.