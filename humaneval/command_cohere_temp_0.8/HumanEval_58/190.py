```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes in two lists, `l1` and `l2`, as parameters. It utilizes the `set` function to remove duplicate elements and inherits the ordering from the original list. The `intersection` method returns elements that are present in both sets. The returned elements are unique and sorted. 

This solution is efficient with time and space complexity of O(m + n) where m and n represent the lengths of the passed in lists. This is because it uses optimized hash-based operations (`set` and `intersection`) that have O(1) average time complexity for operations involving sets. 

This solution provides a straightforward way to solve the problem with minimal syntax and easily passes the provided tests.