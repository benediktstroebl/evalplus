```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes in two lists, `l1` and `l2`, as parameters. It uses the `intersection` method to find the unique elements that appear in both lists, by leveraging the property of sets to contain no duplicate elements. Finally, it sorts the resulting list and returns it. This solves the challenge of finding the sorted unique common elements between the two lists.