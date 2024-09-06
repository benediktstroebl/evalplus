```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes in two lists, `l1` and `l2` and returns the sorted unique elements that are present in both lists. This is done using the `set` data type in Python, which automatically removes duplicate elements. The `intersection` method returns a set of the elements that are present in both sets, and `sort()` is used to ensure that the elements are sorted.