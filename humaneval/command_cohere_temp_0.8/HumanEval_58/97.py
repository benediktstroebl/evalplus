```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `set` function is used to remove duplicate elements from both lists, and `intersection` is used to find the common elements between the two lists. Finally, `sorted` is used to sort the result. This algorithm efficiently solves the problem in a single function, using a straightforward approach.