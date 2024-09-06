```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes two lists, `l1` and `l2` as parameters and returns the sorted unique common elements using the `set` data type to remove duplicates and the `intersection` method to find common elements. Finally, the sorted list is returned using the `sorted` function.