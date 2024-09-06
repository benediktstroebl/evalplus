```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `set` function is used to remove duplicate elements from both lists, and `intersection` retrieves the common elements between the two lists. Finally, `sorted` is applied to organize the result in a sorted way. The creator of the function included some test cases to verify its functionality and a comment to briefly explain the solution.