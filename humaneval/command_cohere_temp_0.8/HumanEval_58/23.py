```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes in two lists, `l1` and `l2`, as parameters. It uses the `set` function to remove duplicate elements and utilizes the `intersection` method to find the common elements in both lists. To ensure uniqueness, the sorted version of the resulting set is returned. This approach ensures the efficiency of the algorithm, as it only requires a single pass to compare the lists and creates minimal additional data structures.