```python
def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists."""
    return sorted(set(l1) & set(l2))

# Test the function
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
print(common([5, 3, 2, 8], [3, 2]))
```

This script uses Python's built-in `set` function to find the intersection of two lists, which then automatically removes duplicates. The `sorted` function is used to sort the resulting list. The `&` operator is used to get the intersection of two sets.

Note that this solution has a time complexity of O(n + m) where n and m are the sizes of the input lists, because it uses the `&` operator to find the intersection, which under the hood uses a hash set. The `set` constructor has a time complexity of O(n) and the `sorted` function has a time complexity of O(n log n).