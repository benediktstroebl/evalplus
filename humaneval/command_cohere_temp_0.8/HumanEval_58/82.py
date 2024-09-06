```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `set` function is used to remove duplicate elements from both lists, and `intersection` returns elements that appear in both adjusted lists. Finally, the result is sorted using the `sorted` function to ensure a consistent order for the returned list. 

This approach ensures that the returned list contains only unique, sorted elements common to both lists, regardless of the initial order or duplicates in the input lists.