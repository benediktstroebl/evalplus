```python
def unique(lst: list):
    """Return sorted unique elements in a list."""
    return sorted(set(lst))

# Example usage:
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
# Output: [0, 2, 3, 5, 9, 123]
```

This script defines a function `unique(lst)` that takes a list as input, converts it to a set (which automatically removes duplicates), and then sorts the resulting set. The sorted unique elements are then returned by the function. The example usage demonstrates how to call the function with the provided list.