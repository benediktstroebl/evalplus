```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    return sorted(set(l))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script works by first converting the list to a set, which automatically removes any duplicate elements. The `set` data structure in Python is an unordered collection of unique elements. Then, it converts the set back to a list and sorts it in ascending order before returning the result.

The time complexity of this solution is O(n), where n is the number of elements in the list, because the `set` data structure has an average time complexity of O(n). The sorting operation also has a time complexity of O(n log n), but it dominates the time complexity of the set operation, so the overall time complexity remains O(n log n).