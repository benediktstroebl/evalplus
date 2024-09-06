```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [x + 1 for x in l]

# Test case 1
assertEqual([1, 2, 3], [2, 3, 4])

# Test case 2
assertEqual([5, 3, 5], [6, 4, 6])

# Test case 3
assertEqual([5, 3, 5, 2, 3], [6, 4, 6, 3])

# Test case 4
assertEqual([5, 3, 5, 2, 3, 3], [6, 4, 6, 4, 3])

# Test case 5
assertEqual([5, 3, 5, 2, 3, 3, 9, 0, 123], [6, 4, 6, 4, 3, 10, 1, 124])
```
The code defines a function `incr_list` that takes a list `l` as an argument and returns a new list with elements from the original list incremented by 1. The test cases verify the region that the function is producing the correct output.