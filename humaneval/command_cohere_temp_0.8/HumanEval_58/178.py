```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes two lists, `l1` and `l2` as parameters and returns the sorted unique elements that are present in both lists. It uses the `set` data type to remove duplicate elements and then uses the `intersection` method to find the common elements between the two lists. Finally, it uses the `sorted` function to sort the result.