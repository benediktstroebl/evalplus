```python
def incr_list(l: list) -> list:
    """Return list with elements incremented by 1."""
    return [i + 1 for i in l]


# Test cases
print(incr_list([1, 2, 3]))  # Expected output: [2, 3, 4]
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # Expected output: [6, 4, 6, 3, 4, 4, 10, 1, 124]
```

This script defines a function `incr_list` that takes a list `l` as input and returns a new list where each element is incremented by 1. The function uses a list comprehension to create a new list with the incremented elements. The test cases demonstrate the function's behavior with different input lists.