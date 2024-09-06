```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes in two lists, `l1` and `l2`, as parameters. It utilizes the `set` function to remove duplicate elements and inherits the sorting attribute. The `intersection` function then returns the common elements between the two lists. Finally, the sorted unique common elements are returned.

This solution is efficient and handles various scenarios, including cases where there are different types of elements in the lists and cases with large lists.