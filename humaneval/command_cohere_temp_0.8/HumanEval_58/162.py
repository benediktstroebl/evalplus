```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes two lists, `l1` and `l2` as parameters and returns the sorted unique common elements using the `set` data type to automatically filter out duplicate elements. Then, the `intersection` method returns the common elements between the two lists, and `sorted` is used to ensure that the output is sorted. 

This solution adheres to the problem statement, specifying the return of common elements in sorted order while excluding duplicates. Although the previous solution used `set` to remove duplicates, the current approach utilizes `set` within the `intersection` method, ensuring the output includes only elements present in both lists.

This improved solution is more concise and functionally correct, guaranteeing that outputs meet the problem requirements.