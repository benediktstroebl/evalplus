```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes in two lists, `l1` and `l2`, as arguments. It uses the `set` function to remove duplicate elements from both lists and then uses the `intersection` method to find the elements that are common in both lists. Finally, it uses the `sorted` function to return the common elements in sorted order.