```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes two lists, `l1` and `l2`, as arguments. It uses the `intersection` method to find the unique elements that appear in both lists, and the `set` function to remove duplicate elements. The result is then sorted using the `sorted` function to ensure a consistent order for the common elements. 

This solution adheres to the problem statement and provides the required functionality in a straightforward manner. You can use the function as defined in the provided code snippet, and it will return the sorted unique common elements for any two lists you pass to it.