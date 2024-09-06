```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes in two lists, `l1` and `l2` and returns the sorted unique elements that are common in both lists. It uses the `set` data type to remove duplicate elements and the `intersection` method to find the common elements between the two lists. Finally, it uses the `sorted` function to return the common elements in a sorted order.