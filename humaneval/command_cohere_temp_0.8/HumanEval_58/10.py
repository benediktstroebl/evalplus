```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `set` function is used to remove duplicate elements from both lists, and `intersection` returns elements that appear in both lists. Finally, `sorted` is applied to organize the result. This approach ensures efficiency and clarity. The function is self-contained and solves the challenge of finding unique common elements in two lists.