```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `set` function is used to remove duplicate elements from both lists, and `intersection` returns elements that appear in both lists. Finally, `sorted` is applied to sort the unique and common elements between the two lists. The resulting output is a sorted list of unique elements that appear in both input lists.