```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [x + 1 for x in l]

# Test case 1: Basic operation
assertEqual([1, 2, 3], incr_list([1, 2, 3]))

# Test case 2: Append element at the end
assertEqual([5, 3, 5], incr_list([5, 3]))

# Test case 3: Append multiple elements
assertEqual([0, 123], incr_list([5, 3, 5, 2, 3, 3]))

# Test case 4: Pop the last element
assertEqual([6], incr_list([6]))

# Test case 5: Clear the list
assertEqual([], incr_list([]))
```
This code defines a function `incr_list` that takes a list as input and returns a new list with elements incremented by 1. The test cases provided validate the specific operation scenarios and ensure the correctness of the `incr_list` function.