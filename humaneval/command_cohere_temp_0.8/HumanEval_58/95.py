```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes two lists, `l1` and `l2`, as arguments. It uses the `intersection` method to find the unique elements that appear in both lists, and the `set` function to remove any duplicate elements. Then it sorts the result using the `sorted` function. This solves the problem of finding the sorted unique common elements for two lists.