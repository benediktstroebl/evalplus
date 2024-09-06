```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `set` function is used to remove duplicate elements from both lists, and `intersection` returns elements present in both adjusted lists. Finally, the result is sorted using the `sorted` function to ensure a consistent order for the resulting list of common elements. 

This approach ensures that the function returns a list of unique, sorted common elements for any two lists passed to the function.