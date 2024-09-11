```python
def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

# Example usage:
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

Explanation:

- The function `unique` takes a list `l` as input.
- It converts the list to a set using `set(l)`, which automatically removes duplicates.
- It then sorts the set using the `sorted` function and returns the result.

This script defines the function `unique` and demonstrates its usage by printing the sorted unique elements of the provided list.