```python
def incr_list(l: list) -> list:
    """Return list with elements incremented by 1."""
    return [x + 1 for x in l]

# Test cases
print(incr_list([1, 2, 3]))
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines a function `incr_list` that takes a list `l` as input and returns a new list where each element from the original list is incremented by 1. The function uses a list comprehension to achieve this. The test cases at the end demonstrate the function's behavior on the provided examples.