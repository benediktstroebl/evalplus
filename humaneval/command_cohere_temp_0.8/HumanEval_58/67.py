```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes two lists, `l1` and `l2` as parameters and returns the sorted unique common elements using the `set` data type to automatically filter out duplicate elements. Then, the `intersection` method returns a set of common elements between the two lists, and `sorted` is used to ensure that the output is sorted. This algorithm allows for efficient and accurate determination of common elements between the two input lists.