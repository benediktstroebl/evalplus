```python
def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

# Example usage
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # Output: [0, 2, 3, 5, 9, 123]
print(unique([4, 4, 2, 1, 6, 6, 5, 3, 3]))   # Output: [1, 2, 3, 4, 5, 6]
```

In this script, the function `unique` utilizes Python's built-in `set` data structure, which automatically removes duplicates, and the `sorted` function to sort the unique elements in ascending order. The example usage demonstrates how to use the `unique` function.