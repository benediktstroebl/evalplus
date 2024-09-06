```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [i+1 for i in l]

# Test case 1: Basic incrementation
assertEqual([1, 2, 3], incr_list([1, 2, 3]))

# Test case 2: Existing element remains unchanged
assertEqual([5, 3, 5], incr_list([5, 3, 5]))

# Test case 3: Recursive call
assertEqual([9, 0, 123], incr_list([9, 0, 123]))

# Test case 4: Lists with duplicates
assertEqual([2, 3, 2], incr_list([2, 3, 2]))
```
This code defines a function `incr_list` that iteratively adds 1 to each element in the input list. It provides several test cases to validate the functionality, ensuring that the output list is correct according to the increment operation.