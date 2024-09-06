```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes two lists, `l1` and `l2` as arguments. It uses the `set` function to remove duplicate elements from both lists and then uses the `intersection` method to find the elements that are common in both sets. The result is sorted to ensure that the output is predictable and stable.