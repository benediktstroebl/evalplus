```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes two lists, `l1` and `l2` as arguments. It uses the `intersection` method to find the unique elements common in both lists, and the `set` function to remove duplicates. The result is then sorted using the `sorted` function to ensure a consistent order for the common elements. 

This solution is efficient with a time complexity of O(min(len(l1), len(l2))).