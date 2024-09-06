```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `set` function is used to remove duplicate elements from both lists, and `intersection` is used to find the common elements between the two sets. Finally, `sorted` is used to sort the result. This solution is efficient with a time complexity of O(M*N) where M and N are the lengths of l1 and l2.