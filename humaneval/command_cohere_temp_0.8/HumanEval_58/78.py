```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes in two lists, `l1` and `l2`, as parameters. It uses the `set` function to remove any duplicate elements and uses the `intersection` method to find the elements that are common in both lists. The resulting list of unique common elements is then sorted using the `sorted` function to ensure a consistent order. 

This solution is efficient with a time complexity of O(m + n) where `m` and `n` are the lengths of l1 and l2 respectively. This is because the intersection operation takes O(n) time for each list, and there are m + n total elements in both input lists.