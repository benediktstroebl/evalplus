```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `set` function is used to remove duplicate elements from both lists, and `intersection` is used to find the common elements between the two lists. Finally, the result is sorted using the `sorted` function to ensure the elements are in ascending order. The result is a list of sorted unique common elements for the two input lists.