```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes in two lists, `l1` and `l2` and returns the sorted unique elements that are present in both lists. This is done using the `set` data type in Python, which automatically removes duplicate elements. The `intersection` method returns a set of the elements that are present in both sets, and `sorted` is subsequently applied to return the elements in a particular ordered arrangement. 

This solution is efficient with a time complexity of O(m + n) where m and n represent the lengths of the two lists. This is because the `set` data type reduces the complexity of list intersection to O(m + n) from the previous O(min(m, n)).