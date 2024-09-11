```python
def incr_list(l: list) -> list:
    """Return list with elements incremented by 1."""
    return [i + 1 for i in l]

# Example usage:
print(incr_list([1, 2, 3]))  # Output: [2, 3, 4]
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # Output: [6, 4, 6, 3, 4, 4, 10, 1, 124]
```

In this script, we define a function `incr_list` that uses a list comprehension to increment each element in the input list by 1. The function returns the resulting list. The example usage demonstrates the function's behavior with two different input lists.