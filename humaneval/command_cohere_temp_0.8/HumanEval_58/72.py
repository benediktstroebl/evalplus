```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes in two lists, `l1` and `l2`, as parameters. It utilizes the `set` function to remove duplicate elements and the `intersection` method to find the elements that are common in both sets. To ensure that the result is sorted, the `sorted` function is used. 

This solution is efficient with time and memory complexity of O(min(len(l1), len(l2))).