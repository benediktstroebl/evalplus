```python
def unique(lst: list) -> list:
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(lst))

# Example usage:
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

Explanation:
- The `set(lst)` expression creates a set from the list, which automatically removes any duplicate elements.
- The `sorted()` function then sorts the set in ascending order, returning the sorted unique elements.
- The function returns this sorted list.

This solution has a time complexity of O(n log n) due to the sorting operation, where n is the number of elements in the list. The set creation operation has a time complexity of O(n), but this is dominated by the sorting operation.