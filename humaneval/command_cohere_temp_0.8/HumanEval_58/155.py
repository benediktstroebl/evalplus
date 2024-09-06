```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes two lists, `l1` and `l2` as arguments. It uses the `set` function to remove duplicate elements from both lists and uses the `intersection` method to find the common elements between the two sets. The `sorted` function is then applied to sort the unique common elements. The resulting list is returned as the output.

This solution is efficient and uses built-in Python functions to solve the problem. It also maintains a unique element property, as shown in the example test cases.