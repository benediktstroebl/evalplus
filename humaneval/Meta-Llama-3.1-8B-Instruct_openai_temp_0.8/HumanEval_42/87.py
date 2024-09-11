```python
def incr_list(l: list) -> list:
    """Return list with elements incremented by 1."""
    return [i + 1 for i in l]

# Test cases
print(incr_list([1, 2, 3]))  # Expected output: [2, 3, 4]
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # Expected output: [6, 4, 6, 3, 4, 4, 10, 1, 124]
```

This script uses a list comprehension to increment each element in the input list by 1. The `-> list` syntax is a type hint indicating that the function returns a list. The test cases are included to demonstrate the function's behavior.