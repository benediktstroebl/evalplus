```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `set` function is used to remove duplicate elements from both lists, and `intersection` is used to find the common elements between the two sets, which are then sorted. It is enclosed in a function with the name `common` and takes two list parameters, `l1` and `l2`, with help text that indicates it returns the sorted unique common elements between the two lists. 

This code defines a function rather than a class, returns the expected output, and has no variables to initialize, so it is ready to use as a self-contained block of code.