```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `set` function is used to remove duplicate elements from both lists, and `intersection` returns elements that appear in both lists. The `sorted` function is then applied to return the elements in a consistent order. 

This solution is efficient with a time complexity of O(M+N) where M and N are the lengths of l1 and l2 respectively, considering the use of the `set` data structure that provides constant time average complexity for insertion and retrieval operations.