```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `set` function is used to remove duplicate elements from both lists, and `intersection` returns elements that appear in both lists. Finally, `sorted` is applied to sort the unique common elements. The code efficiently solves the problem and returns the required output.