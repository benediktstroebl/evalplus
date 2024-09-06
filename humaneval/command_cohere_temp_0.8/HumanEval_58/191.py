```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `set` function is used to remove duplicate elements from both lists, and `intersection` returns elements that appear in both lists. Lastly, `sorted` is applied to keep the elements organized and returned. With this approach, the code achieves a time complexity of `O(min(n, m))`, where `n` and `m` are the lengths of the two lists. This efficiency allows it to handle lengthy lists gracefully.