```python
def unique(lst: list) -> list:
    """Return sorted unique elements in a list"""
    return sorted(set(lst))

# Example usage:
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
# Output: [0, 2, 3, 5, 9, 123]
```

This script defines a function `unique` that takes a list as input, removes duplicates by converting the list to a set, and then returns the sorted list of unique elements. The `sorted` function is used to sort the list in ascending order. The example usage demonstrates how to use this function with the given input list.