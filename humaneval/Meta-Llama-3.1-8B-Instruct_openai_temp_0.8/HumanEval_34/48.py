```python
def unique(lst: list):
    """Return sorted unique elements in a list"""
    return sorted(set(lst))

# Example usage:
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines a function called `unique` that takes a list as input, removes duplicates by converting it to a set (which automatically removes any duplicate elements), and then sorts the resulting set in ascending order using the `sorted` function. The result is a new sorted list with unique elements.

Please note: This function is case-sensitive and assumes that elements in the list are hashable (e.g., not mutable objects like lists or dictionaries). If you need to handle unhashable objects (like lists of lists), you'll need a more complex implementation, possibly involving a custom sorting function.