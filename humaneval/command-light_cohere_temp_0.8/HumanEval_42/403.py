```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test case 1: Basic function call
assert incr_list([1, 2, 3]) == [2, 3, 4]

# Test case 2: Single element list
assert incr_list([5]) == [6]

# Test case 3: Empty list
assert incr_list([]) == []

# Test case 4: List with single element
assert incr_list([3, 7, 9]) == [4, 7, 9]

# Test case 5: List with multiple elements
assert incr_list([5, 3, 5, 2, 3, 3]) == [6, 4, 6, 3, 4, 4, 10, 1]

# Test case 6: List with large numbers
assert incr_list([0, 123, 456, 789, 123]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
```
The function `incr_list` takes a list as input and returns a new list with each element incremented by 1. The test cases cover a basic function usage, empty lists, single elements, and lists with multiple elements.