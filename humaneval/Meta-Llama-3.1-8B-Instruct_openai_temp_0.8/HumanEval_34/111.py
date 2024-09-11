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

This script uses the `set` function to remove duplicates from the list, and the `sorted` function to sort the resulting set. The `set` function returns a new set object, which is an unordered collection of unique elements. The `sorted` function then returns a new sorted list from the elements of the set.

When you run this script, it will print the sorted unique elements in the list: `[0, 2, 3, 5, 9, 123]`.