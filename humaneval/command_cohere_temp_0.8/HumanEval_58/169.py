```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes in two lists, `l1` and `l2`, as parameters. It uses the `set` function to remove duplicate elements and inherits the ordering from the original `list`. The `intersection` method returns a list of elements that are present in both sets. These common elements are then returned. 

This solution is efficient with a time complexity of O(m + n) where m and n represent the lengths of l1 and l2 respectively. This is due to the efficiency of the `set` method in Python.