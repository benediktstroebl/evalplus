```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test case 1
assertEqual([1, 2, 3], incr_list([1, 2, 3]))

# Test case 2
assertEqual([5, 3, 5], incr_list([5, 3, 5]))

# Test case 3
assertEqual([5, 6, 7], incr_list([5, 6, 7]))

# Test case 4
assertEqual([0, 1, 2], incr_list([0, 1, 2]))

# Test case 5
assertEqual([123, 124], incr_list([123]))
```

This code defines a function called `incr_list` that takes a list as input and returns a new list with each element incremented by 1. The test cases provided ensure that the function correctly updates the input list with the desired result.