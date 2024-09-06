```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes in two lists, `l1` and `l2`, as parameters. It utilizes the `set` function to remove duplicate elements and inherits the sorting attribute. The `intersection` function then returns the common elements between the two lists. Lastly, the returned common elements are sorted in alphanumeric order. 

This function fulfills the problem statement in the provided Markdown code block. It outputs sorted unique common elements for any two lists passed into the function.