```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes two lists, `l1` and `l2` as arguments. It uses the `intersection` method to find the unique elements common in both lists, and the `set` function to remove duplicates. The result is then sorted using the `sorted` function to ensure a consistent order for the common elements. 

This solution is efficient with time complexity of O(min(len(l1), len(l2))). This is because the intersection operation and the sorting operation both have a time complexity of O(n log n), and the union operation takes O(m) time, where m is the size of the smaller list.