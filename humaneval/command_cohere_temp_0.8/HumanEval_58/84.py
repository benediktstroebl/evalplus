```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes two lists, `l1` and `l2`, as parameters and returns the sorted unique elements that are common in both lists. It uses the `set` data type to remove duplicate elements and then applies intersection to find the common elements, finally, it sorts the result.