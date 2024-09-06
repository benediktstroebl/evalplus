```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `set` function is used to remove duplicate elements from both lists, and `intersection` returns elements that appear in both lists. Lastly, `sorted` is applied to keep the elements in question in sorted order. This solution is efficient and has a time complexity of O(M+N) where M and N are the lengths of the two lists.