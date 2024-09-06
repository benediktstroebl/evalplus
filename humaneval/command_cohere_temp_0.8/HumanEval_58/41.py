```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes two lists as parameters and uses the `set` function to remove duplicates, then uses the `intersection` method to find the common elements, and finally uses the `sorted` function to sort these common elements. 

This solution is 5 operations total: 3 times the `len` operation, 1 `set` operation, and 1 `sort` operation, so it is relatively efficient for the amount of processing it does. 

Name an alternative approach that preserves the list ordering and uses only 1 additional list comprehension.