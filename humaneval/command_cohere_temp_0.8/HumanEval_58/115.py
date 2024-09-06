```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes two lists as parameters and uses the `set` function to remove duplicate elements from both lists. The `intersection` method is then used to find the common elements between the two sets, which are then sorted using the `sorted` function. This solves the problem of finding unique and sorted common elements between the two lists.