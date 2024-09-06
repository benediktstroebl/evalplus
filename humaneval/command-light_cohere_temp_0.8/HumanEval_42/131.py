```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [i + 1 for i in l]
    return new_list

# Test case 1
assertEqual([1, 2, 3], [2, 3, 4])

# Test case 2
assertEqual([5, 3, 5], [6, 4, 6])

# Test case 3
assertEqual([5, 3, 9], [10, 6, 9])

# Test case 4
assertEqual([0, 123], [1, 124])
```
This Python script defines a function `incr_list` that returns a new list with elements incremented by 1. 

The test cases are provided to verify that the `incr_list` function works as expected.