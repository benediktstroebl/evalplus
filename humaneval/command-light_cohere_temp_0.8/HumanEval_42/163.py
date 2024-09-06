```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test case 1: Basic function call
assert incr_list([1, 2, 3]) == [2, 3, 4]

# Test case 2: List comprehension with increment
assert incr_list([5, 3, 5, 2, 3, 3]) == [6, 4, 6, 3, 4, 4]

# Test case 3: Coconut test
# This one is just for fun!
assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
```
The above Python code defines a function `incr_list` that returns a new list with elements incremented by 1. It is then three test cases to validate the correctness of the function. The test cases cover basic function call, list comprehension with increment, and an edge case with a reversed list and special numbers.