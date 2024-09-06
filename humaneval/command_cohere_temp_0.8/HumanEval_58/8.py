```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `set` function is used to remove duplicate elements from both lists, and `intersection` returns elements that appear in both lists. Finally, `sorted` is applied to output the elements in order. The resulting algorithm executes in O(min(len(l1), len(l2))).