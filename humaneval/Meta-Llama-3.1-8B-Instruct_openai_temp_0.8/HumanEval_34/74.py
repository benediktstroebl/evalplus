```python
def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # Output: [0, 2, 3, 5, 9, 123]
print(unique([1, 1, 2, 2, 3, 3, 4, 4]))  # Output: [1, 2, 3, 4]
print(unique([]))  # Output: []
```

This script uses the built-in Python functions `set()` to create a set from the input list, which automatically removes any duplicate elements. The `sorted()` function is then used to sort the set in ascending order. The result is a sorted list of unique elements.