```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `set` function is used to remove duplicate elements from both lists, and `intersection` returns elements that appear in both lists. Lastly, `sorted` is applied to keep the elements organized and returned. With this approach, the code achieves a time complexity of O(M + N) where M and N represent the lengths of the two lists. This enables efficient computation of the common elements between the two lists in the majority of use cases.