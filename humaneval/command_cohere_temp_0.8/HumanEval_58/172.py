```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes two lists, `l1` and `l2` as arguments. It uses the `intersection` method to find the unique elements common in both lists, and the `set` function to remove duplicate elements. The result is then sorted using the `sorted` function to ensure a consistent order for the returned list. 

This function fulfills the problem requirement to return sorted unique common elements for two input lists.