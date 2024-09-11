```python
def incr_list(l: list) -> list:
    """Return list with elements incremented by 1."""
    return [element + 1 for element in l]

# Test cases
print(incr_list([1, 2, 3]))  # [2, 3, 4]
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # [6, 4, 6, 3, 4, 4, 10, 1, 124]
```

This script defines a function `incr_list` that takes a list as input and returns a new list with each element incremented by 1. It uses a list comprehension to create the new list, which is a concise and efficient way to create lists in Python. The function is then tested with the provided example use cases.