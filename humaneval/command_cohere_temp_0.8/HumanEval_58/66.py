```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes two lists, `l1` and `l2`, as parameters. It uses the `set` function to remove duplicate elements from both lists and then uses the `intersection` method to find the common elements between the two sets. The result is sorted using the `sorted` function to ensure a consistent order for the output.